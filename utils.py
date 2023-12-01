import random

chars = "abcdefghijklmnopqrstuvwxyz0123456789/+"
regions = [
    "us-east-1", "us-east-2", "us-west-1", "us-west-2", "af-south-1", "ap-east-1", "ap-south-1",
    "ap-northeast-1", "ap-northeast-2", "ap-northeast-3", "ap-southeast-1", "ap-southeast-2",
    "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-south-1",
    "eu-north-1", "me-south-1", "sa-east-1"
]


def generate_aws_id():
    """
    Generate a random aws id for access.

    Returns:
        string: aws id.
    """
    return ''.join(random.choice(chars[:36]).upper() for _ in range(16))


def generate_aws_key():
    """
    Generate a random aws key for access.

    Returns:
        string: aws key.
    """
    output = random.choice(chars[:26]).upper()
    output += ''.join(random.choice(chars) for _ in range(38))
    output += random.choice(chars[:26]).upper()
    return output


def generate_aws_region():
    """
    Pick a region from the regions list.

    Returns:
        string: aws region.
    """
    return random.choice(regions)


def generate_access():
    """
    Generates all the necessary credentials for aws access.

    Returns:
        string: aws key for access.
        string: aws id for access.
        string: aws region for access.
    """
    aws_key = generate_aws_key()
    aws_id = generate_aws_id()
    aws_region = generate_aws_region
    return aws_key, aws_id, aws_region
