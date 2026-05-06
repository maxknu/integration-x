# Integration-X — Claude Code Notes

One-shot Python integration: pulls SOAP XML customer drops from an SFTP
inbox and upserts them as Companies in a Twenty CRM workspace.

The repo currently contains the spec only. The implementation will be
generated from `SPEC.md`.

## Authoritative sources

- `SPEC.md` — full spec. §6 has the field mapping, §12 the env vars,
  §13 the target project layout.
- `docs/company.soap.xml` — reference SOAP `ListCompaniesResponse` in the
  exact shape the SFTP inbox produces. Match this when writing the parser.
- `docs/twenty-crm.md` — vendored Twenty REST docs.
- `.agents/skills/twenty-crm/SKILL.md` — REST conventions, filter syntax,
  composite field shapes (`domainName`, `address`, money fields). Read this
  before assuming any Twenty endpoint or field name.

## House rules

- Python 3.11+. Use Polars for the normalize step (declarative, not pandas).
- Never commit secrets. `.env` is gitignored; treat `TWENTY_API_TOKEN` and
  SFTP credentials as secrets and read them from env vars only.
- Dedup by `name` only for v1. A name match means "already present, leave
  untouched" — do not update existing Companies.
- Per-row failures: skip + log, keep going. Per-file failures: surface to
  exit code 1.
- Composite Twenty fields (`domainName`, `address`, money) have specific
  shapes — see the twenty-crm skill, do not guess.

## Layout

The folder previously named `.codex/` is now `.agents/` (tool-agnostic).
The only skill kept is `.agents/skills/twenty-crm/`; the other Symphony-era
skills were pruned because their assumptions (Elixir runtime, Codex review
workflow, Symphony's `linear_graphql` tool) do not hold in this repo.
