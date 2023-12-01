import random
import boto3

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
    aws_region = generate_aws_region()
    return aws_key, aws_id, aws_region


def generate_multiple_access(num_of_keys):
    """
    Generated a certain number of keys.

    Args:
        num_of_keys (int): number of keys to generate.

    Returns:
        list: list of all access keys.
    """
    access_keys = []
    for x in range(0, num_of_keys):
        key, aws_id, region = generate_access()
        access_keys.append([key, aws_id, region, x])
    return access_keys


def check_access_key(key_creds):
    """
    Returns whether or not the aws key and id are valid.

    Args:
        key_creds (list): has aws key and aws id.

    Returns:
        list: the credentials and whether they are valid.
    """
    session = boto3.Session(
        aws_access_key_id=key_creds[1],
        aws_secret_access_key=key_creds[0],
        region_name="us-east-1"
    )
    print("Key creds:", key_creds, "\n", key_creds[1], key_creds[0])

    try:
        sess = session.client('sts')
        print("Session Account:", sess.get_caller_identity().get('Account'))
        key_creds.append("valid")
        return key_creds
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print("Session:", e)
        key_creds.append("invalid")
        return key_creds
