# 14/03/2025
- Options to make inferences of extracted frames located in the s3 bucket: 
- 1. Lambda functions
  2. Sagemaker
 
- Lambda function seems to have a simpler and more cost effective implementation
- Implemented base code for the Lambda function

## Todo
- Make function access frames in s3 bucket
- Put configuration of own s3 bucket
- Schedule to run every time a new frame is detected in s3 bucket
- Test 

# 18/03/2025
- Configured lambda function in aws
- Made firsts test:
- Solved library errors by modifing the requirements file
- Current Error
```
[ERROR] Runtime.ImportModuleError: Unable to import module 'lambda_function': No module named 'onnxruntime.capi.onnxruntime_pybind11_state'
```
- https://www.trainyolo.com/blog/deploy-yolov8-on-aws-lambda

## Todo
- Check possible causes:
- Python version
- Libraries version
- Use SAM to implement whole procedure

# 19/03/2025
- Configured SAM and reconfigured lambda function
- Solved permisssion errors in AWS user (used all available for needed services, might need to leave only the must-have)
- Changed python version from 3.11 to 3.9.21
- Changed versions of requirements libraires
- Forked repo to develop custom code for the application
- Current error:
```
Traceback (most recent call last):  File "/var/runtime/bootstrap.py", line 60, in <module>
main()
File "/var/runtime/bootstrap.py", line 57, in main
awslambdaricmain.main([os.environ["LAMBDA_TASK_ROOT"], os.environ["_HANDLER"]])
File "/var/runtime/awslambdaric/__main__.py", line 21, in main
bootstrap.run(app_root, handler, lambda_runtime_api_addr)
File "/var/runtime/awslambdaric/bootstrap.py", line 497, in run
request_handler = _get_handler(handler)
File "/var/runtime/awslambdaric/bootstrap.py", line 53, in _get_handler
m = importlib.import_module(modname.replace("/", "."))
File "/var/lang/lib/python3.9/importlib/__init__.py", line 127, in import_module
return _bootstrap._gcd_import(name[level:], package, level)
File "/var/task/app.py", line 1, in <module>
from yolo_onnx.yolov8_onnx import YOLOv8
File "/var/task/yolo_onnx/yolov8_onnx.py", line 1, in <module>
import onnxruntime
File "/var/task/onnxruntime/__init__.py", line 23, in <module>
from onnxruntime.capi._pybind_state import ExecutionMode  # noqa: F401
File "/var/task/onnxruntime/capi/_pybind_state.py", line 32, in <module>
from .onnxruntime_pybind11_state import *  # noqa
AttributeError: _ARRAY_API not found
ImportError: numpy.core.multiarray failed to import
The above exception was the direct cause of the following exception:
SystemError: <built-in function __import__> returned a result with an error set
START RequestId: 88ea7d05-610c-46f5-9d6a-b354f6209651 Version: $LATEST
LAMBDA_WARNING: Unhandled exception. The most likely cause is an issue in the function code. However, in rare cases, a Lambda runtime update can cause unexpected function behavior. For functions using managed runtimes, runtime updates can be triggered by a function change, or can be applied automatically. To determine if the runtime has been updated, check the runtime version in the INIT_START log entry. If this error correlates with a change in the runtime version, you may be able to mitigate this error by temporarily rolling back to the previous runtime version. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html
[ERROR] KeyError: 'body'
Traceback (most recent call last):
  File "/var/task/app.py", line 13, in main
    body = json.loads(event['body'])
```
- Analysis and possible solution from AmazonQ
```
Analysis
The error message indicates that the Lambda function is unable to find the 'body' key in the event object passed to the function. This suggests that the input data being passed to the function does not have the expected structure or format.
```
```
1. Review the Lambda function code:
   - Open the Lambda function 'people-counting-YOLOV8Function-ELz4sr3ve5ZU' in the AWS Lambda console
   - Navigate to the 'Code' tab
   - Locate the `main` function in the `app.py` file

2. Modify the event handling:
   - Update the code to handle cases where the 'body' key might not be present in the event
   - Add a check for the existence of the 'body' key before accessing it
   - Example modification:
     ```python
     def main(event, context):
         if 'body' not in event:
             return {
                 'statusCode': 400,
                 'body': json.dumps('Missing body in the event')
             }
         body = json.loads(event['body'])
         # Rest of the function code
     ```

3. Address the NumPy version compatibility issue:
   - In the Lambda function configuration, scroll down to the 'Runtime settings' section
   - Click 'Edit' and change the runtime to 'Python 3.8' (which is compatible with NumPy 1.x)
   - Click 'Save' to apply the changes

4. Update the function's dependencies:
   - In the Lambda function 'Code' tab, scroll down to the 'Runtime settings' section
   - Click on 'Edit' next to 'Layers'
   - Add a layer that includes compatible versions of NumPy, onnxruntime, and other required libraries
   - If a suitable layer doesn't exist, create a new one with the compatible library versions

5. Test the Lambda function:
   - In the Lambda console, go to the 'Test' tab
   - Create a new test event that includes a 'body' key with a JSON string value
   - Run the test to verify that the function now handles the input correctly

6. If you don't have permissions to do the following changes, contact your AWS Administrator:
   - Request to update the IAM role 'people-counting-YOLOV8FunctionRole-Kg1AxRQDEJIx' with the following inline policy:
     ```json
     {
         "Version": "2012-10-17",
         "Statement": [
             {
                 "Effect": "Allow",
                 "Action": [
                     "logs:CreateLogGroup",
                     "logs:CreateLogStream",
                     "logs:PutLogEvents"
                 ],
                 "Resource": "arn:aws:logs:us-east-1:615299755417:log-group:/aws/lambda/people-counting-YOLOV8Function-ELz4sr3ve5ZU:*"
             }
         ]
     }
     ```

7. Monitor the function:
   - After making these changes, test the function again
   - Check the CloudWatch logs for any remaining errors or issues
```
## Todo: 
- Check functionality of app.py and debug
- Check possible compatibility issues with libraries
- Test with test_api.py
- Test using s3 images
