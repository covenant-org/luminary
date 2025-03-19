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
