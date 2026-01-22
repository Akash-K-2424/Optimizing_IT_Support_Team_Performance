# Power BI Files

This folder contains Power BI files for the IT Support Team Performance Optimization project.

## Files

Place your Power BI files here:
- **IT_Support_Performance.pbix** - Main Power BI dashboard file

## Dashboard Components

### 1. Overview Dashboard
- Key performance metrics
- Ticket volume trends
- Team performance summary

### 2. Performance Analysis Dashboard
- Individual team member performance
- Response time analysis
- Resolution time trends
- Customer satisfaction metrics

### 3. Workload Distribution Dashboard
- Ticket distribution across team members
- Priority level analysis
- Issue category breakdown
- Time-based workload patterns

## How to Use

1. Download and install Power BI Desktop from [Microsoft Power BI](https://powerbi.microsoft.com/desktop/)
2. Open the .pbix file in Power BI Desktop
3. Refresh data connections to load the latest processed data from the `Data/processed` folder
4. Explore the dashboards and visualizations
5. Export reports as needed

## Data Source Configuration

The Power BI file is configured to use:
- Data source: CSV files from `../Data/processed/`
- Connection type: File system
- Refresh schedule: Manual or scheduled (when published to Power BI Service)

## Publishing

To publish the dashboard to Power BI Service:
1. Sign in to Power BI Desktop with your organizational account
2. Click "Publish" in the Home ribbon
3. Select your workspace
4. Configure data refresh settings in the Power BI Service

## Requirements

- Power BI Desktop (latest version)
- Access to the processed data files
- Power BI Service account (for online publishing)
