import sys
import boto3
myNamespace = sys.argv[1]
string_to_remove = sys.argv[2]

print "retrieving cloudwatch metrics for namespace " + myNamespace
print "remove this substring from all cloudwatch metric-names: " + string_to_remove

client = boto3.client('cloudwatch')
response = client.list_metrics(
    Namespace = myNamespace
)

header = """{
  "columns": [
    {
      "text": "Total",
      "value": "total"
    }
  ],
  "datasource": "is24-data-pro",
  "editable": true,
  "error": false,
  "fontSize": "80%",
  "id": 23,
  "isNew": true,
  "links": [],
  "pageSize": null,
  "scroll": true,
  "showHeader": true,
  "sort": {
    "col": null,
    "desc": false
  },
  "span": 4,
  "styles": [
    {
      "dateFormat": "YYYY-MM-DD HH:mm:ss",
      "pattern": "Time",
      "type": "date"
    },
    {
      "colorMode": "cell",
      "colors": [
        "rgba(50, 172, 45, 0.97)",
        "rgba(237, 129, 40, 0.89)",
        "rgba(245, 54, 54, 0.9)"
      ],
      "decimals": 0,
      "pattern": "/.*/",
      "thresholds": [
        "1",
        "2"
      ],
      "type": "number",
      "unit": "none"
    }
  ],"""



footer= """  
  "title": "%s",
  "transform": "timeseries_aggregations",
  "type": "table"
}""" % (myNamespace)

 
targets = ""
for i, x in enumerate(sorted(response.get("Metrics"))):
	metricName = x.get("MetricName")
	metricAlias = metricName.replace(string_to_remove,"")
	targets = targets +  """
      {
      "refId": "%s",
      "namespace": "%s",      
      "metricName": "%s",
      "statistics": [
        "Sum"
      ],
      "alias": "%s",
      "dimensions": {},
      "period": "",
      "region": "eu-west-1"},""" % (i, myNamespace,metricName, metricAlias)
targets = targets[:-1]


target_tag = """
		"targets": [
     %s
  ],
""" % (targets)

print "***************************************************************************************************"
print "*********************  COPY JSON PANEL FOR GRAFANA TABLE FROM HERE ********************************"
print "***************************************************************************************************"

print  header + target_tag + footer