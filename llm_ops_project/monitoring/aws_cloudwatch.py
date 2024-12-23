import boto3

cloudwatch = boto3.client('cloudwatch', region_name='us-west-2')

def put_custom_metric(metric_name, value, unit='Count'):
    response = cloudwatch.put_metric_data(
        Namespace='LLMOps',
        MetricData=[
            {
                'MetricName': metric_name,
                'Value': value,
                'Unit': unit
            }
        ]
    )
    print(f"Metric {metric_name} pushed: {response}")

def log_error_to_cloudwatch(log_group, log_stream, message):
    logs = boto3.client('logs', region_name='us-west-2')
    response = logs.put_log_events(
        logGroupName=log_group,
        logStreamName=log_stream,
        logEvents=[
            {
                'timestamp': int(time.time() * 1000),
                'message': message
            }
        ]
    )
    print(f"Logged to CloudWatch: {response}")
