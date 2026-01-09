# Python-project
As a cloud engineer, we take care of the AWS environment and ensure it is in compliance with organizational policies.

In this project we use ``AWS cloud watch`` and ``Lambda function AWS`` to govern the resource according to the policies.

For instance, we trigger a lambda when an Elastic Blob Storage
(EBS) was created. We use Cloud Watch events that allow us to monitor and respond to EBS volumes that are of type GP2 and convert them to GP3.

Let's say someone wants to create an EBS with type GP2 and your organization wants everyone to create an EBS with the type GP3 because of performance issues, then there's a new developer creating an EBS Volume using the type of GP2 and Lambda will trigger and convert it to GP3.

# Prerequisite for this project
- Create and Configure Cloud watch → Go to CW, Events, Rules and create new rules. For service name, choose EC2, event type (ebs volume notification), create a specific event (createVolume) and choose any volume ARN.
- Create an IAM policy for ec2.service → add permission and set up action for all ec2 action if it fails set volumes for actions (List and modify) for resources (All resources)