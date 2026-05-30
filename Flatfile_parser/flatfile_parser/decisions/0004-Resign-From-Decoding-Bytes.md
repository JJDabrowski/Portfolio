## Context

Some fields in file validation are made from whitespaces. String type contracts the whitespaces to just one and disallows to check the length of the field content

## Considered Options

* use bytes to check the `"reserved"` fields length
* resign from validating reserved length

## Decision Outcome

Chosen option: resign from validation reserved length. This app should be simple and easy to talk about, not validate everything to the small detail