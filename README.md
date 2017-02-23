# mySnippets
useful snippets for me

## AWS

### generate-grafana-panel-for-cloudwatch-metrics.py

Use this to present all cloudwatch metrics for a custom namespace on grafana

For a bunch of cloudwatch metrics you don't want to link all of them manually to a grafana dashboard.
This scripts generates the panel json for a grafana table that holds *all* cloudwatch metrics for the provides cloudwatch namespace.
Each row represents the total/sum aggregation.


Examples:
```
python generate-grafana-panel-for-cloudwatch-metrics.py myNamespace StringToRemove
python generate-grafana-panel-for-cloudwatch-metrics.py myNamespace ""
```