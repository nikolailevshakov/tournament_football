#!/bin/bash

TIME="10"
URL="https://api.telegram.org/bot$TELEGRAM_TOKEN/sendMessage"
TEXT="Deploy status: $1%0A%0AProject:+$CI_PROJECT_NAME%0AURL:+$CI_PROJECT_URL/pipelines/$CI_PIPELINE_ID/%0ABranch:+$CI_COMMIT_REF_SLUG%0AUser:+$GITLAB_USER_NAME"
curl -s --max-time $TIME -d "chat_id=$CHAT_ID&text=$TEXT" $URL