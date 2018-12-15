# Zappa based Alexa Skillset hosted on AWS Lambda 

Using Alexa Skills Kit, we can create compelling, hands-free voice experiences by adding our skills to Alexa. Users can access these capabilities on any Alexa-enabled device by merely asking Alexa a question.

### Architecture
![Image of Architecture](https://github.com/davidjegan/Alexa-zappa-based-serverless-bot/blob/master/Architecture/aws_alexa.png)




### Explanation
The user interacts with the Alexa device to trigger the skill set. This customized skill set, written using Flask-ask framework of Python resides in the AWS Lambda and is accessible via the API Gateway. The contents of the interaction model reside in the in-house DynamoDB, and the S3 storage is utilized to archive the documents. The user can initiate a mailing module, which delivers the mail using AWS Simple Notification Service.



### Steps

**Lambda code setup**
1. Install required python package using, `pip install awscli virtualenv flask-ask zappa`
2. (Optional) `aws configure` can be used to provide access and secret key
3. Create a folder using `mkdir flask-zappa-alexa` 
4. Move to the folder directly with `cd flask-zappa-alexa`
5. Start the virtual environment using `source venv/bin/activate`. This is for Mac 
6. Create a file `vi main.py`
7. Upload the [code](Alexa-AWS-Serverless-Voicebot-v0/Lambda/main.py) into the file `main.py`
8. Initialize zappa with `zappa init`. Use default 'yes' for all entries
9. Deploy zappa using `zappa deploy dev` where dev stands for the stage/environment
10. Write down the endpoint obtained from this link
   ```sh
   https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev
   ```
11. (Optional) Inorder to redeploy the code after changes, update zappa using `zappa update dev`

**Alexa skill set creation**
1. Create an Alexa application using this [tutorial](https://developer.amazon.com/alexa-skills-kit/tutorials/fact-skill-1)
	- Follow the [step 1](https://developer.amazon.com/alexa-skills-kit/tutorials/fact-skill-1) completely
	- Skip [step 2](https://developer.amazon.com/alexa-skills-kit/tutorials/fact-skill-2)
	- In [step 3](https://developer.amazon.com/alexa-skills-kit/tutorials/fact-skill-3) use HTTPS. Enter the API Gateway endpoint obtained in step 10 in this phase. 
	- Similarly, follow the [step 4](https://developer.amazon.com/alexa-skills-kit/tutorials/fact-skill-4) completely
	- Skip the [step 5](https://developer.amazon.com/alexa-skills-kit/tutorials/fact-skill-5) and [step 6](https://developer.amazon.com/alexa-skills-kit/tutorials/fact-skill-6) completely

**Testing**
* [Echosim.io](https://echosim.io) - a browser-based Alexa skill testing tool that makes it easy to test your skills without carrying a physical device everywhere you go.
* Unit Testing with Alexa - a modern approach to unit testing your Alexa skills with [Postman](https://www.getpostman.com/) and [Amazon API Gateway](https://aws.amazon.com/api-gateway/)


### Problems addressed
* As websites store more and more information, users often find it harder and harder to get to what they want. 
* Some users (those with visual impairment / accessing from a mobile) see the great graphics layout of most websites off-putting. 
* The cost of maintenance of web page along with customer service agent is much higher in the traditional model
* The adoption of naive and niche technology is required to keep pace with the growing technology

### Services 
![Image of Architecture](https://github.com/davidjegan/Alexa-zappa-based-serverless-bot/blob/master/Architecture/services.jpg)

### Advantages
1. Increased customer satisfaction 
2. Reduced Cost of ownership
3. Increased revenue
4. Win more customers

### References
- [Amazon Alexa](https://developer.amazon.com/alexa)
- [Lambda](http://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [DynamoDB](https://aws.amazon.com/documentation/dynamodb/)
- [API Gateway](https://aws.amazon.com/documentation/apigateway/)
- [S3](https://aws.amazon.com/documentation/s3/)
- [SNS](https://aws.amazon.com/documentation/sns/)

### Authors
* [SS Malvika](https://github.com/SSMalvika "SSMalvika's Github page")
* [David Jegan Abishek](https://github.com/davidjegan "David's Github page")
