# mySnippets
useful snippets for me


## Intellij Idea shortcuts

| mac   | key combination      |
| ------------- |:--------------:|
| CTRL + J        | quick docu     |
| SHIFT + CMD + 8 | column mode             |
| CMD+ALT+L       | formatting              |
| CMD+F12         | quick structure of class or file in editor      |
| CMD+H           | hierarchy of class      |
| CTRL+O          | override methods        |
| CTRL+ENTER      | generate                |
| ALT+ENTER       | add type annotation     |

## Mac shortcuts

| mac   | key combination      |
| ------------- |:--------------:|
| open .       | open terminal path in finder     |
| ~	    |  ALT+N        |
| |     |  ALT+7           |
| \	    |  SHIFT+ALT+7 |
| @     |  ALT+L           |


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