import pulumi
import pulumi_aws as aws


def notes_bucket():
    notes_bucket = aws.s3.Bucket(
        "notes-rosstimson-pulumi",
        acl="private",
        versioning=aws.s3.BucketVersioningArgs(enabled=True, mfa_delete=True),
        server_side_encryption_configuration=aws.s3.BucketServerSideEncryptionConfigurationArgs(
            rule=aws.s3.BucketServerSideEncryptionConfigurationRuleArgs(
                bucket_key_enabled=True,
                apply_server_side_encryption_by_default=aws.s3.BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs(
                    sse_algorithm="AES256",
                ),
            ),
        ),
    )
