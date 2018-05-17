from cortex_client import InputMessage, OutputMessage


def main(params):
    # Parse the function params
    msg = InputMessage.from_params(params)

    # Get text and payload
    text = msg.payload.get('text')

    # Compute and create output
    return OutputMessage.create().with_type('cortex/Text').with_payload({'text': text}).to_params()