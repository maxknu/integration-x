Twenty Api
Download OpenAPI Document

Use this page to explore and call the REST API.
Authentication

Send a Bearer token with each request:

Authorization: Bearer <token>

Example cURL:

curl -H 'Authorization: Bearer <token>' <server>/rest/core/companies

Tokens can be generated in Settings → Playground and are workspace-scoped.
Filters

Use the filter query parameter to narrow results.

    Format: field[COMPARATOR]:value
    Multiple conditions: field1[eq]:1,field2[gte]:10 (root conjunction is AND)
    Composite fields: field.subField[COMPARATOR]:value
    Common comparators: eq, neq, in, containsAny, is, gt, gte, lt, lte, startsWith, like, ilike
    Wildcards: For like/ilike, use % as a wildcard (e.g. %value% for substring match)

Examples:

filter=status[eq]:"open"
filter=createdAt[gte]:"2024-01-01"
filter=owner.name[ilike]:"%smith%"
filter=id[in]:["id-1","id-2"]
filter=deletedAt[is]:NULL
filter=isActive[eq]:true

Advanced (optional): and(...), or(...), not(...) (not wraps one condition)

filter=or(status[eq]:"open",assigneeId[is]:NULL)

Notes: Strings and dates are quoted; numbers are not.
Pagination and ordering

All list endpoints use cursor-based pagination.

    Use limit to cap page size (default: 60, max: 60).
    Use starting_after to fetch the next page (forward).
    Use ending_before to fetch the previous page (backward).
    Responses include pageInfo with hasNextPage, startCursor, and endCursor.

Examples:

# First page
curl -H 'Authorization: Bearer <token>' \
  '<server>/rest/core/companies?limit=60'

# Next page
curl -H 'Authorization: Bearer <token>' \
  '<server>/rest/core/companies?limit=60&starting_after=<endCursorFromPreviousPage>'

# Previous page
curl -H 'Authorization: Bearer <token>' \
  '<server>/rest/core/companies?limit=60&ending_before=<startCursorFromCurrentPage>'

You can combine pagination with filters and ordering.

Ordering with order_by:

    Shape: field1,field2[DIRECTION2]
    Directions: AscNullsFirst, AscNullsLast, DescNullsFirst, DescNullsLast
    Default per-field direction: AscNullsFirst

Examples:

order_by=createdAt
order_by=id[AscNullsFirst],createdAt[DescNullsLast]

Usage with LLMs

You can use AI to generate code based on the OpenAPI schema with the following URLs:

Core: https://crm.mspixel.se/rest/open-api/core?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiZDExY2UzYi0wYmFhLTQyZTYtYTk4YS04MmRkN2ViNDlkM2EiLCJ0eXBlIjoiQVBJX0tFWSIsIndvcmtzcGFjZUlkIjoiYmQxMWNlM2ItMGJhYS00MmU2LWE5OGEtODJkZDdlYjQ5ZDNhIiwiaWF0IjoxNzc2MTA1MjM5LCJleHAiOjE4MDc2NDEyMzcsImp0aSI6Ijc3MWNmY2E1LTRjYzQtNDc4MS04Y2NkLTNiOWFhMDhlNTZlYyJ9.WRz3ZMS1l5Vl1sVrv5Aii1UHuFT8sDCUz53CjVdaxUg
Metadata: https://crm.mspixel.se/rest/open-api/metadata?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiZDExY2UzYi0wYmFhLTQyZTYtYTk4YS04MmRkN2ViNDlkM2EiLCJ0eXBlIjoiQVBJX0tFWSIsIndvcmtzcGFjZUlkIjoiYmQxMWNlM2ItMGJhYS00MmU2LWE5OGEtODJkZDdlYjQ5ZDNhIiwiaWF0IjoxNzc2MTA1MjM5LCJleHAiOjE4MDc2NDEyMzcsImp0aSI6Ijc3MWNmY2E1LTRjYzQtNDc4MS04Y2NkLTNiOWFhMDhlNTZlYyJ9.WRz3ZMS1l5Vl1sVrv5Aii1UHuFT8sDCUz53CjVdaxUg

Quick prompt example (Cursor or any agent):

Here is an OpenAPI schema for the Twenty REST API:
https://crm.mspixel.se/rest/open-api/core?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiZDExY2UzYi0wYmFhLTQyZTYtYTk4YS04MmRkN2ViNDlkM2EiLCJ0eXBlIjoiQVBJX0tFWSIsIndvcmtzcGFjZUlkIjoiYmQxMWNlM2ItMGJhYS00MmU2LWE5OGEtODJkZDdlYjQ5ZDNhIiwiaWF0IjoxNzc2MTA1MjM5LCJleHAiOjE4MDc2NDEyMzcsImp0aSI6Ijc3MWNmY2E1LTRjYzQtNDc4MS04Y2NkLTNiOWFhMDhlNTZlYyJ9.WRz3ZMS1l5Vl1sVrv5Aii1UHuFT8sDCUz53CjVdaxUg

Use it to list companies created after 2024-01-01, ordered by createdAt desc, and include only 20 results.

Notes:

    Treat the token like a secret; prefer a short-lived Playground token.
    Most editors can fetch and process the schema even if it's large.


--
Find Many companies​

order_by, filter, limit, depth, starting_after or ending_before can be provided to request your companies
Query Parameters

    order_by
    Type:string

    Format: **field_name_1,field_name_2[DIRECTION_2] Refer to the filter section at the top of the page for more details.
    filter
    Type:string

    Format: field[COMPARATOR]:value,field2[COMPARATOR]:value2. For like/ilike, use % as a wildcard (e.g. %value% for substring match). Refer to the filter section at the top of the page for more details.
    limit
    Type:integer
    min: 
    0
    max: 
    200
    default: 
    60

    Limits the number of objects returned.
    depth
    Type:integer enum
    default: 
    1

    Determines the level of nested related objects to include in the response. - 0: Primary object only - 1: Primary object + direct relations
        0
        1
    starting_after
    Type:string

    Returns objects starting after a specific cursor. You can find cursors in startCursor and endCursor in pageInfo in response data
    ending_before
    Type:string

    Returns objects ending before a specific cursor. You can find cursors in startCursor and endCursor in pageInfo in response data

Responses

Request Example forGET/companies
Selected HTTP client: Shell Curl

curl https://crm.mspixel.se/rest/companies \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiZDExY2UzYi0wYmFhLTQyZTYtYTk4YS04MmRkN2ViNDlkM2EiLCJ0eXBlIjoiQVBJX0tFWSIsIndvcmtzcGFjZUlkIjoiYmQxMWNlM2ItMGJhYS00MmU2LWE5OGEtODJkZDdlYjQ5ZDNhIiwiaWF0IjoxNzc2MTA1MjM5LCJleHAiOjE4MDc2NDEyMzcsImp0aSI6Ijc3MWNmY2E1LTRjYzQtNDc4MS04Y2NkLTNiOWFhMDhlNTZlYyJ9.WRz3ZMS1l5Vl1sVrv5Aii1UHuFT8sDCUz53CjVdaxUg'

{
  "data": {
    "companies": [
      {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "createdAt": "2026-04-13T18:38:39.995Z",
        "updatedAt": "2026-04-13T18:38:39.995Z",
        "deletedAt": "2026-04-13T18:38:39.995Z",
        "name": "…",
        "domainName": {
          "primaryLinkLabel": "…",
          "primaryLinkUrl": "…",
          "secondaryLinks": [
            {
              "url": "https://example.com",
              "label": "…"
            }
          ]
        },
        "address": {
          "addressStreet1": "…",
          "addressStreet2": "…",
          "addressCity": "…",
          "addressPostcode": "…",
          "addressState": "…",
          "addressCountry": "…",
          "addressLat": 1,
          "addressLng": 1
        },
        "employees": 1,
        "linkedinLink": {
          "primaryLinkLabel": "…",
          "primaryLinkUrl": "…",
          "secondaryLinks": [
            {
              "url": "https://example.com",
              "label": "…"
            }
          ]
        },
        "xLink": {
          "primaryLinkLabel": "…",
          "primaryLinkUrl": "…",
          "secondaryLinks": [
            {
              "url": "https://example.com",
              "label": "…"
            }
          ]
        },
        "annualRecurringRevenue": {
          "amountMicros": 1,
          "currencyCode": "…"
        },
        "idealCustomerProfile": true,
        "position": 1,
        "createdBy": {
          "source": "EMAIL",
          "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
          "name": "…"
        },
        "updatedBy": {
          "source": "EMAIL",
          "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
          "name": "…"
        },
        "accountOwnerId": "123e4567-e89b-12d3-a456-426614174000",
        "currentWorkatoCustomer": true,
        "annualLicenseCommitment": {
          "amountMicros": 1,
          "currencyCode": "…"
        },
        "estimatedHoursPerMonth": 1,
        "attachments": [
          {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "createdAt": "2026-04-13T18:38:39.995Z",
            "updatedAt": "2026-04-13T18:38:39.995Z",
            "deletedAt": "2026-04-13T18:38:39.995Z",
            "name": "…",
            "file": [
              {
                "fileId": "123e4567-e89b-12d3-a456-426614174000",
                "label": "…",
                "extension": "…",
                "url": "…"
              }
            ],
            "fullPath": "…",
            "fileCategory": "ARCHIVE",
            "createdBy": {
              "source": "EMAIL",
              "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
              "name": "…"
            },
            "updatedBy": {
              "source": "EMAIL",
              "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
              "name": "…"
            },
            "position": 1,
            "targetTaskId": "123e4567-e89b-12d3-a456-426614174000",
            "targetNoteId": "123e4567-e89b-12d3-a456-426614174000",
            "targetPersonId": "123e4567-e89b-12d3-a456-426614174000",
            "targetCompanyId": "123e4567-e89b-12d3-a456-426614174000",
            "targetOpportunityId": "123e4567-e89b-12d3-a456-426614174000",
            "targetDashboardId": "123e4567-e89b-12d3-a456-426614174000",
            "targetWorkflowId": "123e4567-e89b-12d3-a456-426614174000",
            "targetTask": "[Circular Reference]",
            "targetNote": "[Circular Reference]",
            "targetPerson": "[Circular Reference]",
            "targetCompany": "[Circular Reference]",
            "targetOpportunity": "[Circular Reference]",
            "targetDashboard": "[Circular Reference]",
            "targetWorkflow": "[Circular Reference]"
          }
        ],
        "people": [
          {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "createdAt": "2026-04-13T18:38:39.995Z",
            "updatedAt": "2026-04-13T18:38:39.995Z",
            "deletedAt": "2026-04-13T18:38:39.995Z",
            "name": {
              "firstName": "…",
              "lastName": "…"
            },
            "emails": {
              "primaryEmail": "…",
              "additionalEmails": [
                "hello@example.com"
              ]
            },
            "linkedinLink": {
              "primaryLinkLabel": "…",
              "primaryLinkUrl": "…",
              "secondaryLinks": [
                {
                  "url": "https://example.com",
                  "label": "…"
                }
              ]
            },
            "xLink": {
              "primaryLinkLabel": "…",
              "primaryLinkUrl": "…",
              "secondaryLinks": [
                {
                  "url": "https://example.com",
                  "label": "…"
                }
              ]
            },
            "jobTitle": "…",
            "phones": {
              "additionalPhones": [
                "…"
              ],
              "primaryPhoneCountryCode": "…",
              "primaryPhoneCallingCode": "…",
              "primaryPhoneNumber": "…"
            },
            "city": "…",
            "avatarUrl": "…",
            "avatarFile": [
              {
                "fileId": "123e4567-e89b-12d3-a456-426614174000",
                "label": "…",
                "extension": "…",
                "url": "…"
              }
            ],
            "position": 1,
            "createdBy": {
              "source": "EMAIL",
              "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
              "name": "…"
            },
            "updatedBy": {
              "source": "EMAIL",
              "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
              "name": "…"
            },
            "companyId": "123e4567-e89b-12d3-a456-426614174000",
            "attachments": "[Circular Reference]",
            "calendarEventParticipants": "[Circular Reference]",
            "company": "[Circular Reference]",
            "favorites": "[Circular Reference]",
            "messageParticipants": "[Circular Reference]",
            "noteTargets": "[Circular Reference]",
            "pointOfContactForOpportunities": "[Circular Reference]",
            "taskTargets": "[Circular Reference]",
            "timelineActivities": "[Circular Reference]"
          }
        ],
        "accountOwner": {
          "id": "123e4567-e89b-12d3-a456-426614174000",
          "createdAt": "2026-04-13T18:38:39.995Z",
          "updatedAt": "2026-04-13T18:38:39.995Z",
          "deletedAt": "2026-04-13T18:38:39.995Z",
          "position": 1,
          "name": {
            "firstName": "…",
            "lastName": "…"
          },
          "colorScheme": "…",
          "locale": "…",
          "avatarUrl": "…",
          "userEmail": "…",
          "calendarStartDay": 1,
          "userId": "123e4567-e89b-12d3-a456-426614174000",
          "timeZone": "…",
          "dateFormat": "SYSTEM",
          "timeFormat": "SYSTEM",
          "numberFormat": "SYSTEM",
          "createdBy": {
            "source": "EMAIL",
            "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "name": "…"
          },
          "updatedBy": {
            "source": "EMAIL",
            "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "name": "…"
          },
          "blocklist": "[Circular Reference]",
          "calendarEventParticipants": "[Circular Reference]",
          "accountOwnerForCompanies": "[Circular Reference]",
          "connectedAccounts": "[Circular Reference]",
          "favorites": "[Circular Reference]",
          "messageParticipants": "[Circular Reference]",
          "ownedOpportunities": "[Circular Reference]",
          "assignedTasks": "[Circular Reference]",
          "timelineActivities": "[Circular Reference]"
        },
        "taskTargets": [
          {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "createdAt": "2026-04-13T18:38:39.995Z",
            "updatedAt": "2026-04-13T18:38:39.995Z",
            "deletedAt": "2026-04-13T18:38:39.995Z",
            "createdBy": {
              "source": "EMAIL",
              "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
              "name": "…"
            },
            "updatedBy": {
              "source": "EMAIL",
              "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
              "name": "…"
            },
            "position": 1,
            "targetCompanyId": "123e4567-e89b-12d3-a456-426614174000",
            "targetPersonId": "123e4567-e89b-12d3-a456-426614174000",
            "targetOpportunityId": "123e4567-e89b-12d3-a456-426614174000",
            "taskId": "123e4567-e89b-12d3-a456-426614174000",
            "targetCompany": "[Circular Reference]",
            "targetPerson": "[Circular Reference]",
            "targetOpportunity": "[Circular Reference]",
            "task": "[Circular Reference]"
          }
        ],
        "noteTargets": [
          {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "createdAt": "2026-04-13T18:38:39.995Z",
            "updatedAt": "2026-04-13T18:38:39.995Z",
            "deletedAt": "2026-04-13T18:38:39.995Z",
            "createdBy": {
              "source": "EMAIL",
              "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
              "name": "…"
            },
            "updatedBy": {
              "source": "EMAIL",
              "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
              "name": "…"
            },
            "position": 1,
            "targetCompanyId": "123e4567-e89b-12d3-a456-426614174000",
            "noteId": "123e4567-e89b-12d3-a456-426614174000",
            "targetPersonId": "123e4567-e89b-12d3-a456-426614174000",
            "targetOpportunityId": "123e4567-e89b-12d3-a456-426614174000",
            "targetCompany": "[Circular Reference]",
            "note": "[Circular Reference]",
            "targetPerson": "[Circular Reference]",
            "targetOpportunity": "[Circular Reference]"
          }
        ],
        "opportunities": [
          {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "createdAt": "2026-04-13T18:38:39.995Z",
            "updatedAt": "2026-04-13T18:38:39.995Z",
            "deletedAt": "2026-04-13T18:38:39.995Z",
            "name": "…",
            "amount": {
              "amountMicros": 1,
              "currencyCode": "…"
            },
            "closeDate": "2026-04-13T18:38:39.995Z",
            "stage": "NEW",
            "position": 1,
            "createdBy": {
              "source": "EMAIL",
              "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
              "name": "…"
            },
            "updatedBy": {
              "source": "EMAIL",
              "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
              "name": "…"
            },
            "companyId": "123e4567-e89b-12d3-a456-426614174000",
            "pointOfContactId": "123e4567-e89b-12d3-a456-426614174000",
            "ownerId": "123e4567-e89b-12d3-a456-426614174000",
            "attachments": "[Circular Reference]",
            "company": "[Circular Reference]",
            "favorites": "[Circular Reference]",
            "noteTargets": "[Circular Reference]",
            "pointOfContact": "[Circular Reference]",
            "taskTargets": "[Circular Reference]",
            "timelineActivities": "[Circular Reference]",
            "owner": "[Circular Reference]"
          }
        ],
        "favorites": [
          {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "createdAt": "2026-04-13T18:38:39.995Z",
            "updatedAt": "2026-04-13T18:38:39.995Z",
            "deletedAt": "2026-04-13T18:38:39.995Z",
            "createdBy": {
              "source": "EMAIL",
              "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
              "name": "…"
            },
            "updatedBy": {
              "source": "EMAIL",
              "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
              "name": "…"
            },
            "position": 1,
            "viewId": "123e4567-e89b-12d3-a456-426614174000",
            "companyId": "123e4567-e89b-12d3-a456-426614174000",
            "dashboardId": "123e4567-e89b-12d3-a456-426614174000",
            "forWorkspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "personId": "123e4567-e89b-12d3-a456-426614174000",
            "opportunityId": "123e4567-e89b-12d3-a456-426614174000",
            "workflowId": "123e4567-e89b-12d3-a456-426614174000",
            "workflowVersionId": "123e4567-e89b-12d3-a456-426614174000",
            "workflowRunId": "123e4567-e89b-12d3-a456-426614174000",
            "taskId": "123e4567-e89b-12d3-a456-426614174000",
            "noteId": "123e4567-e89b-12d3-a456-426614174000",
            "favoriteFolderId": "123e4567-e89b-12d3-a456-426614174000",
            "company": "[Circular Reference]",
            "dashboard": "[Circular Reference]",
            "forWorkspaceMember": "[Circular Reference]",
            "person": "[Circular Reference]",
            "opportunity": "[Circular Reference]",
            "workflow": "[Circular Reference]",
            "workflowVersion": "[Circular Reference]",
            "workflowRun": "[Circular Reference]",
            "task": "[Circular Reference]",
            "note": "[Circular Reference]",
            "favoriteFolder": "[Circular Reference]"
          }
        ],
        "timelineActivities": [
          {
            "updatedBy": {
              "source": "EMAIL",
              "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
              "name": "…"
            },
            "position": 1,
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "createdAt": "2026-04-13T18:38:39.995Z",
            "updatedAt": "2026-04-13T18:38:39.995Z",
            "deletedAt": "2026-04-13T18:38:39.995Z",
            "createdBy": {
              "source": "EMAIL",
              "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
              "name": "…"
            },
            "happensAt": "2026-04-13T18:38:39.995Z",
            "name": "…",
            "properties": {},
            "linkedRecordCachedName": "…",
            "linkedRecordId": "123e4567-e89b-12d3-a456-426614174000",
            "linkedObjectMetadataId": "123e4567-e89b-12d3-a456-426614174000",
            "targetCompanyId": "123e4567-e89b-12d3-a456-426614174000",
            "targetDashboardId": "123e4567-e89b-12d3-a456-426614174000",
            "targetNoteId": "123e4567-e89b-12d3-a456-426614174000",
            "targetOpportunityId": "123e4567-e89b-12d3-a456-426614174000",
            "targetPersonId": "123e4567-e89b-12d3-a456-426614174000",
            "targetTaskId": "123e4567-e89b-12d3-a456-426614174000",
            "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "targetWorkflowId": "123e4567-e89b-12d3-a456-426614174000",
            "targetWorkflowVersionId": "123e4567-e89b-12d3-a456-426614174000",
            "targetWorkflowRunId": "123e4567-e89b-12d3-a456-426614174000",
            "targetCompany": "[Circular Reference]",
            "targetDashboard": "[Circular Reference]",
            "targetNote": "[Circular Reference]",
            "targetOpportunity": "[Circular Reference]",
            "targetPerson": "[Circular Reference]",
            "targetTask": "[Circular Reference]",
            "workspaceMember": "[Circular Reference]",
            "targetWorkflow": "[Circular Reference]",
            "targetWorkflowVersion": "[Circular Reference]",
            "targetWorkflowRun": "[Circular Reference]"
          }
        ]
      }
    ]
  },
  "pageInfo": {
    "hasNextPage": true,
    "startCursor": "123e4567-e89b-12d3-a456-426614174000",
    "endCursor": "123e4567-e89b-12d3-a456-426614174000"
  },
  "totalCount": 1
}

Successful operation
Create One company​
Query Parameters

    depth
    Type:integer enum
    default: 
    1

    Determines the level of nested related objects to include in the response. - 0: Primary object only - 1: Primary object + direct relations
        0
        1
    upsert
    Type:boolean
    default: 
    false

    If true, creates the object or updates it if it already exists.

Body
application/json

A company

    name
    Type:string

    The company name
    domainName
    Type:object

    The company website URL. We use this url to fetch the company icon
    address
    Type:object

    Address of the company
    employees
    Type:integer

    Number of employees in the company
    linkedinLink
    Type:object

    The company Linkedin account
    xLink
    Type:object

    The company Twitter/X account
    annualRecurringRevenue
    Type:object

    Annual Recurring Revenue: The actual or estimated annual revenue of the company
    idealCustomerProfile
    Type:boolean

    Ideal Customer Profile: Indicates whether the company is the most suitable and valuable customer for you
    position
    Type:number

    Company record position
    createdBy
    Type:object

    The creator of the record
    updatedBy
    Type:object

    The workspace member who last updated the record
    accountOwnerId
    Type:string Format: uuid
    currentWorkatoCustomer
    Type:boolean
    annualLicenseCommitment
    Type:object
    estimatedHoursPerMonth
    Type:integer

    Integer numbers.

Responses

Request Example forPOST/companies
Selected HTTP client: Shell Curl

curl https://crm.mspixel.se/rest/companies \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiZDExY2UzYi0wYmFhLTQyZTYtYTk4YS04MmRkN2ViNDlkM2EiLCJ0eXBlIjoiQVBJX0tFWSIsIndvcmtzcGFjZUlkIjoiYmQxMWNlM2ItMGJhYS00MmU2LWE5OGEtODJkZDdlYjQ5ZDNhIiwiaWF0IjoxNzc2MTA1MjM5LCJleHAiOjE4MDc2NDEyMzcsImp0aSI6Ijc3MWNmY2E1LTRjYzQtNDc4MS04Y2NkLTNiOWFhMDhlNTZlYyJ9.WRz3ZMS1l5Vl1sVrv5Aii1UHuFT8sDCUz53CjVdaxUg' \
  --data '{
  "name": "Company name",
  "domainName": {
    "primaryLinkLabel": "",
    "primaryLinkUrl": "https://short-term-teriyaki.net/",
    "secondaryLinks": []
  },
  "linkedinLink": {
    "primaryLinkLabel": "",
    "primaryLinkUrl": "https://profitable-trash.name",
    "secondaryLinks": []
  },
  "xLink": {
    "primaryLinkLabel": "",
    "primaryLinkUrl": "https://anguished-vision.net/",
    "secondaryLinks": []
  },
  "annualRecurringRevenue": {
    "amountMicros": "402000000",
    "currencyCode": "EUR"
  },
  "annualLicenseCommitment": {
    "amountMicros": "123000000",
    "currencyCode": "EUR"
  }
}'

{
  "data": {
    "createCompany": {
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "createdAt": "2026-04-13T18:38:39.995Z",
      "updatedAt": "2026-04-13T18:38:39.995Z",
      "deletedAt": "2026-04-13T18:38:39.995Z",
      "name": "…",
      "domainName": {
        "primaryLinkLabel": "…",
        "primaryLinkUrl": "…",
        "secondaryLinks": [
          {
            "url": "https://example.com",
            "label": "…"
          }
        ]
      },
      "address": {
        "addressStreet1": "…",
        "addressStreet2": "…",
        "addressCity": "…",
        "addressPostcode": "…",
        "addressState": "…",
        "addressCountry": "…",
        "addressLat": 1,
        "addressLng": 1
      },
      "employees": 1,
      "linkedinLink": {
        "primaryLinkLabel": "…",
        "primaryLinkUrl": "…",
        "secondaryLinks": [
          {
            "url": "https://example.com",
            "label": "…"
          }
        ]
      },
      "xLink": {
        "primaryLinkLabel": "…",
        "primaryLinkUrl": "…",
        "secondaryLinks": [
          {
            "url": "https://example.com",
            "label": "…"
          }
        ]
      },
      "annualRecurringRevenue": {
        "amountMicros": 1,
        "currencyCode": "…"
      },
      "idealCustomerProfile": true,
      "position": 1,
      "createdBy": {
        "source": "EMAIL",
        "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
        "name": "…"
      },
      "updatedBy": {
        "source": "EMAIL",
        "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
        "name": "…"
      },
      "accountOwnerId": "123e4567-e89b-12d3-a456-426614174000",
      "currentWorkatoCustomer": true,
      "annualLicenseCommitment": {
        "amountMicros": 1,
        "currencyCode": "…"
      },
      "estimatedHoursPerMonth": 1,
      "attachments": [
        {
          "id": "123e4567-e89b-12d3-a456-426614174000",
          "createdAt": "2026-04-13T18:38:39.995Z",
          "updatedAt": "2026-04-13T18:38:39.995Z",
          "deletedAt": "2026-04-13T18:38:39.995Z",
          "name": "…",
          "file": [
            {
              "fileId": "123e4567-e89b-12d3-a456-426614174000",
              "label": "…",
              "extension": "…",
              "url": "…"
            }
          ],
          "fullPath": "…",
          "fileCategory": "ARCHIVE",
          "createdBy": {
            "source": "EMAIL",
            "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "name": "…"
          },
          "updatedBy": {
            "source": "EMAIL",
            "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "name": "…"
          },
          "position": 1,
          "targetTaskId": "123e4567-e89b-12d3-a456-426614174000",
          "targetNoteId": "123e4567-e89b-12d3-a456-426614174000",
          "targetPersonId": "123e4567-e89b-12d3-a456-426614174000",
          "targetCompanyId": "123e4567-e89b-12d3-a456-426614174000",
          "targetOpportunityId": "123e4567-e89b-12d3-a456-426614174000",
          "targetDashboardId": "123e4567-e89b-12d3-a456-426614174000",
          "targetWorkflowId": "123e4567-e89b-12d3-a456-426614174000",
          "targetTask": "[Circular Reference]",
          "targetNote": "[Circular Reference]",
          "targetPerson": "[Circular Reference]",
          "targetCompany": "[Circular Reference]",
          "targetOpportunity": "[Circular Reference]",
          "targetDashboard": "[Circular Reference]",
          "targetWorkflow": "[Circular Reference]"
        }
      ],
      "people": [
        {
          "id": "123e4567-e89b-12d3-a456-426614174000",
          "createdAt": "2026-04-13T18:38:39.995Z",
          "updatedAt": "2026-04-13T18:38:39.995Z",
          "deletedAt": "2026-04-13T18:38:39.995Z",
          "name": {
            "firstName": "…",
            "lastName": "…"
          },
          "emails": {
            "primaryEmail": "…",
            "additionalEmails": [
              "hello@example.com"
            ]
          },
          "linkedinLink": {
            "primaryLinkLabel": "…",
            "primaryLinkUrl": "…",
            "secondaryLinks": [
              {
                "url": "https://example.com",
                "label": "…"
              }
            ]
          },
          "xLink": {
            "primaryLinkLabel": "…",
            "primaryLinkUrl": "…",
            "secondaryLinks": [
              {
                "url": "https://example.com",
                "label": "…"
              }
            ]
          },
          "jobTitle": "…",
          "phones": {
            "additionalPhones": [
              "…"
            ],
            "primaryPhoneCountryCode": "…",
            "primaryPhoneCallingCode": "…",
            "primaryPhoneNumber": "…"
          },
          "city": "…",
          "avatarUrl": "…",
          "avatarFile": [
            {
              "fileId": "123e4567-e89b-12d3-a456-426614174000",
              "label": "…",
              "extension": "…",
              "url": "…"
            }
          ],
          "position": 1,
          "createdBy": {
            "source": "EMAIL",
            "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "name": "…"
          },
          "updatedBy": {
            "source": "EMAIL",
            "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "name": "…"
          },
          "companyId": "123e4567-e89b-12d3-a456-426614174000",
          "attachments": "[Circular Reference]",
          "calendarEventParticipants": "[Circular Reference]",
          "company": "[Circular Reference]",
          "favorites": "[Circular Reference]",
          "messageParticipants": "[Circular Reference]",
          "noteTargets": "[Circular Reference]",
          "pointOfContactForOpportunities": "[Circular Reference]",
          "taskTargets": "[Circular Reference]",
          "timelineActivities": "[Circular Reference]"
        }
      ],
      "accountOwner": {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "createdAt": "2026-04-13T18:38:39.995Z",
        "updatedAt": "2026-04-13T18:38:39.995Z",
        "deletedAt": "2026-04-13T18:38:39.995Z",
        "position": 1,
        "name": {
          "firstName": "…",
          "lastName": "…"
        },
        "colorScheme": "…",
        "locale": "…",
        "avatarUrl": "…",
        "userEmail": "…",
        "calendarStartDay": 1,
        "userId": "123e4567-e89b-12d3-a456-426614174000",
        "timeZone": "…",
        "dateFormat": "SYSTEM",
        "timeFormat": "SYSTEM",
        "numberFormat": "SYSTEM",
        "createdBy": {
          "source": "EMAIL",
          "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
          "name": "…"
        },
        "updatedBy": {
          "source": "EMAIL",
          "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
          "name": "…"
        },
        "blocklist": "[Circular Reference]",
        "calendarEventParticipants": "[Circular Reference]",
        "accountOwnerForCompanies": "[Circular Reference]",
        "connectedAccounts": "[Circular Reference]",
        "favorites": "[Circular Reference]",
        "messageParticipants": "[Circular Reference]",
        "ownedOpportunities": "[Circular Reference]",
        "assignedTasks": "[Circular Reference]",
        "timelineActivities": "[Circular Reference]"
      },
      "taskTargets": [
        {
          "id": "123e4567-e89b-12d3-a456-426614174000",
          "createdAt": "2026-04-13T18:38:39.995Z",
          "updatedAt": "2026-04-13T18:38:39.995Z",
          "deletedAt": "2026-04-13T18:38:39.995Z",
          "createdBy": {
            "source": "EMAIL",
            "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "name": "…"
          },
          "updatedBy": {
            "source": "EMAIL",
            "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "name": "…"
          },
          "position": 1,
          "targetCompanyId": "123e4567-e89b-12d3-a456-426614174000",
          "targetPersonId": "123e4567-e89b-12d3-a456-426614174000",
          "targetOpportunityId": "123e4567-e89b-12d3-a456-426614174000",
          "taskId": "123e4567-e89b-12d3-a456-426614174000",
          "targetCompany": "[Circular Reference]",
          "targetPerson": "[Circular Reference]",
          "targetOpportunity": "[Circular Reference]",
          "task": "[Circular Reference]"
        }
      ],
      "noteTargets": [
        {
          "id": "123e4567-e89b-12d3-a456-426614174000",
          "createdAt": "2026-04-13T18:38:39.995Z",
          "updatedAt": "2026-04-13T18:38:39.995Z",
          "deletedAt": "2026-04-13T18:38:39.995Z",
          "createdBy": {
            "source": "EMAIL",
            "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "name": "…"
          },
          "updatedBy": {
            "source": "EMAIL",
            "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "name": "…"
          },
          "position": 1,
          "targetCompanyId": "123e4567-e89b-12d3-a456-426614174000",
          "noteId": "123e4567-e89b-12d3-a456-426614174000",
          "targetPersonId": "123e4567-e89b-12d3-a456-426614174000",
          "targetOpportunityId": "123e4567-e89b-12d3-a456-426614174000",
          "targetCompany": "[Circular Reference]",
          "note": "[Circular Reference]",
          "targetPerson": "[Circular Reference]",
          "targetOpportunity": "[Circular Reference]"
        }
      ],
      "opportunities": [
        {
          "id": "123e4567-e89b-12d3-a456-426614174000",
          "createdAt": "2026-04-13T18:38:39.995Z",
          "updatedAt": "2026-04-13T18:38:39.995Z",
          "deletedAt": "2026-04-13T18:38:39.995Z",
          "name": "…",
          "amount": {
            "amountMicros": 1,
            "currencyCode": "…"
          },
          "closeDate": "2026-04-13T18:38:39.995Z",
          "stage": "NEW",
          "position": 1,
          "createdBy": {
            "source": "EMAIL",
            "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "name": "…"
          },
          "updatedBy": {
            "source": "EMAIL",
            "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "name": "…"
          },
          "companyId": "123e4567-e89b-12d3-a456-426614174000",
          "pointOfContactId": "123e4567-e89b-12d3-a456-426614174000",
          "ownerId": "123e4567-e89b-12d3-a456-426614174000",
          "attachments": "[Circular Reference]",
          "company": "[Circular Reference]",
          "favorites": "[Circular Reference]",
          "noteTargets": "[Circular Reference]",
          "pointOfContact": "[Circular Reference]",
          "taskTargets": "[Circular Reference]",
          "timelineActivities": "[Circular Reference]",
          "owner": "[Circular Reference]"
        }
      ],
      "favorites": [
        {
          "id": "123e4567-e89b-12d3-a456-426614174000",
          "createdAt": "2026-04-13T18:38:39.995Z",
          "updatedAt": "2026-04-13T18:38:39.995Z",
          "deletedAt": "2026-04-13T18:38:39.995Z",
          "createdBy": {
            "source": "EMAIL",
            "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "name": "…"
          },
          "updatedBy": {
            "source": "EMAIL",
            "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "name": "…"
          },
          "position": 1,
          "viewId": "123e4567-e89b-12d3-a456-426614174000",
          "companyId": "123e4567-e89b-12d3-a456-426614174000",
          "dashboardId": "123e4567-e89b-12d3-a456-426614174000",
          "forWorkspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
          "personId": "123e4567-e89b-12d3-a456-426614174000",
          "opportunityId": "123e4567-e89b-12d3-a456-426614174000",
          "workflowId": "123e4567-e89b-12d3-a456-426614174000",
          "workflowVersionId": "123e4567-e89b-12d3-a456-426614174000",
          "workflowRunId": "123e4567-e89b-12d3-a456-426614174000",
          "taskId": "123e4567-e89b-12d3-a456-426614174000",
          "noteId": "123e4567-e89b-12d3-a456-426614174000",
          "favoriteFolderId": "123e4567-e89b-12d3-a456-426614174000",
          "company": "[Circular Reference]",
          "dashboard": "[Circular Reference]",
          "forWorkspaceMember": "[Circular Reference]",
          "person": "[Circular Reference]",
          "opportunity": "[Circular Reference]",
          "workflow": "[Circular Reference]",
          "workflowVersion": "[Circular Reference]",
          "workflowRun": "[Circular Reference]",
          "task": "[Circular Reference]",
          "note": "[Circular Reference]",
          "favoriteFolder": "[Circular Reference]"
        }
      ],
      "timelineActivities": [
        {
          "updatedBy": {
            "source": "EMAIL",
            "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "name": "…"
          },
          "position": 1,
          "id": "123e4567-e89b-12d3-a456-426614174000",
          "createdAt": "2026-04-13T18:38:39.995Z",
          "updatedAt": "2026-04-13T18:38:39.995Z",
          "deletedAt": "2026-04-13T18:38:39.995Z",
          "createdBy": {
            "source": "EMAIL",
            "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
            "name": "…"
          },
          "happensAt": "2026-04-13T18:38:39.995Z",
          "name": "…",
          "properties": {},
          "linkedRecordCachedName": "…",
          "linkedRecordId": "123e4567-e89b-12d3-a456-426614174000",
          "linkedObjectMetadataId": "123e4567-e89b-12d3-a456-426614174000",
          "targetCompanyId": "123e4567-e89b-12d3-a456-426614174000",
          "targetDashboardId": "123e4567-e89b-12d3-a456-426614174000",
          "targetNoteId": "123e4567-e89b-12d3-a456-426614174000",
          "targetOpportunityId": "123e4567-e89b-12d3-a456-426614174000",
          "targetPersonId": "123e4567-e89b-12d3-a456-426614174000",
          "targetTaskId": "123e4567-e89b-12d3-a456-426614174000",
          "workspaceMemberId": "123e4567-e89b-12d3-a456-426614174000",
          "targetWorkflowId": "123e4567-e89b-12d3-a456-426614174000",
          "targetWorkflowVersionId": "123e4567-e89b-12d3-a456-426614174000",
          "targetWorkflowRunId": "123e4567-e89b-12d3-a456-426614174000",
          "targetCompany": "[Circular Reference]",
          "targetDashboard": "[Circular Reference]",
          "targetNote": "[Circular Reference]",
          "targetOpportunity": "[Circular Reference]",
          "targetPerson": "[Circular Reference]",
          "targetTask": "[Circular Reference]",
          "workspaceMember": "[Circular Reference]",
          "targetWorkflow": "[Circular Reference]",
          "targetWorkflowVersion": "[Circular Reference]",
          "targetWorkflowRun": "[Circular Reference]"
        }
      ]
    }
  }
}

Successful operation
Delete Many companies​
Query Parameters

    filter
    Type:string

    Format: field[COMPARATOR]:value,field2[COMPARATOR]:value2. For like/ilike, use % as a wildcard (e.g. %value% for substring match). Refer to the filter section at the top of the page for more details.
    soft_delete
    Type:boolean
    default: 
    false

    If true, soft deletes the objects. If false, objects are permanently deleted.

Responses

Request Example forDELETE/companies
Selected HTTP client: Shell Curl

curl https://crm.mspixel.se/rest/companies \
  --request DELETE \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiZDExY2UzYi0wYmFhLTQyZTYtYTk4YS04MmRkN2ViNDlkM2EiLCJ0eXBlIjoiQVBJX0tFWSIsIndvcmtzcGFjZUlkIjoiYmQxMWNlM2ItMGJhYS00MmU2LWE5OGEtODJkZDdlYjQ5ZDNhIiwiaWF0IjoxNzc2MTA1MjM5LCJleHAiOjE4MDc2NDEyMzcsImp0aSI6Ijc3MWNmY2E1LTRjYzQtNDc4MS04Y2NkLTNiOWFhMDhlNTZlYyJ9.WRz3ZMS1l5Vl1sVrv5Aii1UHuFT8sDCUz53CjVdaxUg'

{
  "data": {
    "deleteCompanies": [
      {
        "id": "123e4567-e89b-12d3-a456-426614174000"
      }
    ]
  }
}

Successful operation
Update Many companies​
Query Parameters

    depth
    Type:integer enum
    default: 
    1

    Determines the level of nested related objects to include in the response. - 0: Primary object only - 1: Primary object + direct relations
        0
        1
    filter
    Type:string

    Format: field[COMPARATOR]:value,field2[COMPARATOR]:value2. For like/ilike, use % as a wildcard (e.g. %value% for substring match). Refer to the filter section at the top of the page for more details.

Body
application/json

A company

    name
    Type:string

    The company name
    domainName
    Type:object

    The company website URL. We use this url to fetch the company icon
    address
    Type:object

    Address of the company
    employees
    Type:integer

    Number of employees in the company
    linkedinLink
    Type:object

    The company Linkedin account
    xLink
    Type:object

    The company Twitter/X account
    annualRecurringRevenue
    Type:object

    Annual Recurring Revenue: The actual or estimated annual revenue of the company
    idealCustomerProfile
    Type:boolean

    Ideal Customer Profile: Indicates whether the company is the most suitable and valuable customer for you
    position
    Type:number

    Company record position
    createdBy
    Type:object

    The creator of the record
    updatedBy
    Type:object

    The workspace member who last updated the record
    accountOwnerId
    Type:string Format: uuid
    currentWorkatoCustomer
    Type:boolean
    annualLicenseCommitment
    Type:object
    estimatedHoursPerMonth
    Type:integer

    Integer numbers.

Responses





