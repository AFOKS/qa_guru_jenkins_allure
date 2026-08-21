# отчет allure
allure serve ./allure-results

# рабочий запуск
pytest -s jenkins_with_params/tests/test_registration_form.py \
    --browser=chrome \
    --browser-version=149.0

# Headless
pytest -s jenkins_with_params/tests/test_registration_form.py \
    --browser=chrome \
    --browser-version=149.0 \
    --headless

# Другое разрешение
pytest -s jenkins_with_params/tests/test_registration_form.py \
    --browser=chrome \
    --browser-version=149.0 \
    --resolution=1280x720

# Другой сайт

pytest -s jenkins_with_params/tests/test_registration_form.py \
    --site-url="https://demoqa.com/automation-practice-form"

pytest -s jenkins_with_params/tests/test_registration_form.py \
    --browser=$BROWSER
    --browser-version=$BROWSER_VERSION
    --headless=$HEADLESS

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest . pytest -s jenkins_with_params/tests/test_registration_form.py \
    --browser=$BROWSER
    --browser-version=$BROWSER_VERSION
    --headless=$HEADLESS

python -m venv .venv
source .venv/bin/activate

python -m pip install -r requirements.txt

python -m pytest -s jenkins_with_params/tests/test_registation_form.py \
    --browser="$BROWSER" \
    --browser-version="$BROWSER_VERSION" \
    #--alluredir=allure-results

{
  "base": {
    "project": "${JOB_BASE_NAME}",
    "environment": "some env",
    "comment": "some comment",
    "reportLink": "${BUILD_URL}",
    "language": "en",
    "allureFolder": "allure-report",
    "enableChart": true
  },
  "telegram": {
    "token": "8999793890:AAFjHe_-DI4_iweIQjjA3uOtsXRW9mu70gs",
    "chat": "-1002259275993",
    "replyTo": ""
  }
}

echo "===== NETWORK ====="

echo "--- DNS ---"
getent hosts api.telegram.org || true

echo "--- IPv4 ---"
curl -4 -v --connect-timeout 10 https://api.telegram.org/ || true

echo "--- IPv6 ---"
curl -6 -v --connect-timeout 10 https://api.telegram.org/ || true

echo "===== NOTIFICATION ====="

java -DconfigFile=notifications/config.json \
     -jar notifications/allure-notifications-4.6.1.jar


1

mkdir -p notifications

FILE=notifications/allure-notifications-4.6.1.jar

if [ ! -f "$FILE" ]; then
    wget -O "$FILE" \
      https://github.com/qa-guru/allure-notifications/releases/download/4.6.1/allure-notifications-4.6.1.jar
fi

echo "===== CURRENT DIRECTORY ====="
pwd

echo "===== NOTIFICATIONS ====="
ls -la notifications

echo "===== ALLURE REPORT ====="
ls -la allure-report
ls -la allure-report/widgets

echo "===== SUMMARY ====="
ls -l allure-report/widgets/summary.json

echo "===== START NOTIFICATIONS ====="

java -DconfigFile=notifications/config.json \
     -jar notifications/allure-notifications-4.6.1.jar

2

mkdir -p notifications

FILE=notifications/allure-notifications-4.6.1.jar

if [ ! -f "$FILE" ]; then
    wget -O "$FILE" \
      https://github.com/qa-guru/allure-notifications/releases/download/4.6.1/allure-notifications-4.6.1.jar
fi

echo "===== CURRENT DIRECTORY ====="
pwd

echo "===== NOTIFICATIONS ====="
ls -la notifications

echo "===== ALLURE REPORT ====="
ls -la allure-report
ls -la allure-report/widgets

echo "===== SUMMARY ====="
ls -l allure-report/widgets/summary.json

echo "===== START NOTIFICATIONS ====="

java -DconfigFile=notifications/config.json \
     -jar notifications/allure-notifications-4.6.1.jar


# конфиг

cd "${WORKSPACE}"

test -f allure-report/widgets/summary.json || {
    echo "No Allure summary — skip Telegram"
    exit 0
}

echo "===== RAW CONFIG ====="
cat -n notifications/config.json

echo "===== JSON VALIDATION ====="
python -m json.tool notifications/config.json

echo "===== PREPARE PROXY ====="

 /opt/qa-guru/bin/prepare-telegram-socks-proxy.sh \
    notifications/config.json \
    /tmp/proxychains-telegram.conf

echo "===== CHECK ALLURE ====="

ls -lh allure-report/widgets/summary.json

echo "===== ALLURE FILES ====="

find allure-report -maxdepth 2 -type f | sort

echo "===== SEND TELEGRAM ====="

proxychains4 -q -f /tmp/proxychains-telegram.conf \
    npx \
    --package @qa-guru/allure-notifications@6.2.2 \
    -- \
    allure-notifications send \
    --config notifications/config.json \
    --live