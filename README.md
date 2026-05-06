# Integration-X

A one-shot Python integration that reads Customer records from an SFTP drop
folder (SOAP XML) and upserts them as Companies in a Twenty CRM workspace.

> [!NOTE]
> This repo currently contains the specification only. The implementation
> will be generated from `SPEC.md` using a coding agent.

## What it does

1. Connects to an SFTP server and lists `*.xml` files in a configured inbox.
2. Parses each file as a SOAP `ListCompaniesResponse` envelope (see
   `docs/company.soap.xml` for the reference shape).
3. Standardizes the rows in a Polars DataFrame (trim, normalize, in-batch
   dedup by `name`).
4. For each row, looks up an existing Twenty Company by exact `name`. If
   none exists, creates one with `name`, `domainName`, and `address`.
5. Moves successfully processed files to `<inbox>/processed/`.
6. Writes a per-run log to `<inbox>/log/<UTC ISO8601>.log`.

The CLI runs once and exits. Scheduling is handled by an external job
runner (cron, systemd timer, etc.). See [`SPEC.md`](SPEC.md) for the
authoritative description.

## Building it with a coding agent

The recommended path is to let Codex (or another coding agent) implement
Integration-X from the spec, the same way the upstream Symphony project
recommends. The repo already includes:

- [`SPEC.md`](SPEC.md) — the integration spec.
- [`.codex/skills/twenty-crm/SKILL.md`](.codex/skills/twenty-crm/SKILL.md)
  — a reusable skill describing the Twenty REST API.
- [`docs/company.soap.xml`](docs/company.soap.xml) — a reference input
  file in the exact format the SFTP inbox produces.
- [`docs/twenty-crm.md`](docs/twenty-crm.md) — vendored Twenty API docs.
- [`docs/crm.png`](docs/crm.png) — screenshot of the target Twenty
  workspace.

Open the repo in Codex and prompt:

> Implement Integration-X according to `SPEC.md`. Use Python 3.11+ with
> Polars for the data normalization step. Follow the project layout in
> §13 and the field mapping in §6. Use `.codex/skills/twenty-crm/SKILL.md`
> for Twenty REST conventions. Do not commit any secrets.

## Running it (once implemented)

```bash
python -m integration_x
```

The CLI takes no required arguments. All configuration comes from
environment variables (full list in `SPEC.md` §12).

Required:

| Variable           | Example                  |
|--------------------|--------------------------|
| `SFTP_HOST`        | `192.168.1.98`           |
| `SFTP_PORT`        | `2022`                   |
| `SFTP_USERNAME`    | `viipipe`                |
| `SFTP_PASSWORD`    | (secret)                 |
| `SFTP_INBOX`       | `ERPOut`                 |
| `TWENTY_BASE_URL`  | `https://crm.mspixel.se` |
| `TWENTY_API_TOKEN` | (secret)                 |

Optional:

| Variable                        | Default | Notes                          |
|---------------------------------|---------|--------------------------------|
| `INTEGRATION_X_TIMEOUT_SECONDS` | `30`    | Per-HTTP-request timeout.      |
| `INTEGRATION_X_LOG_LEVEL`       | `INFO`  | `INFO` or `DEBUG`.             |

A `.env` file may be used during development. Make sure it is in
`.gitignore` and never committed.

Exit codes:

- `0` — every file processed (per-row skips are allowed and logged).
- `1` — at least one file-level failure (parse, archive, or log upload).

## Project layout

See `SPEC.md` §13 for the full target tree. Today the repo contains:

```
.
├── SPEC.md
├── README.md
├── docs/
│   ├── company.soap.xml
│   ├── twenty-crm.md
│   └── crm.png
└── .codex/
    └── skills/twenty-crm/SKILL.md
```

## License

Apache License 2.0 — see [`LICENSE`](LICENSE).
