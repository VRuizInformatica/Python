GET /pm-kpis
As a portfolio manager, I want to retrieve KPI results for the securitized pool
So that I can monitor performance and detect changes between periods

GET /pm-filters
As a portfolio manager, I want to obtain the list of available grid filters (column + type)
So that I can build dynamic filter menus in the front-end

GET /securitized-assets
As a portfolio manager, I want to fetch a paginated list of securitized contracts
So that I can review the current pool composition

GET /no-meet-criteria
As a portfolio manager, I want to retrieve assets that do not meet eligibility criteria
So that I can analyse the reasons for their exclusion

GET /last-reference-date
As a portfolio manager, I want to know the latest cut-off date stored in the database
So that I can display the “Last pool update” timestamp to users

GET /manual-removals
As a verification agent, I want to list assets marked for manual removal with their metadata
So that I can audit and validate manual changes applied to the pool

GET /download-securitized-assets
As a portfolio manager, I want to download securitized-asset data as a CSV file
So that I can analyse it offline and share it with stakeholders

GET /download-no-meet-criteria
As a portfolio manager, I want to download the list of assets that do not meet criteria as a CSV file
So that I can review and archive the exclusions in external tools
