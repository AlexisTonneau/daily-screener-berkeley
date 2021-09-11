# Auto Daily Screener 

Enables to fill automatically COVID-19 Daily Screener of UC Berkeley. _You must have a CalNet ID_

**DO NOT USE IT IF YOU DON'T MATCH THE FOLLOWING CRITERIAS !** 
- You will be on campus today.
- You don't have any [COVID-19 symptom](https://www.cdc.gov/coronavirus/2019-ncov/symptoms-testing/symptoms.html).
- You don't live with or have had close contact with anyone who has tested positive for COVID-19 in the past 14 days.
- You are fully vaccinated against COVID-19 (at least 2 weeks from last dose)
- You haven't had a positive COVID-19 test

## How-to
You have 5 seconds to accept Duo Mobile push notification to succeed !
#### iOS
Use [this iOS shortcut here.](https://www.icloud.com/shortcuts/484e0f810792436f836bc5f31c7e56c7)
If it's your first time using iOS shortcuts, please follow [this tutorial](https://support.apple.com/guide/shortcuts/enable-shared-shortcuts-apdfeb05586f/ios)

#### Android
I don't have immediate solution for Android, apart from using directly the API :
```
curl  -H "Content-Type: application/json" --request POST --data '{"username":"<your-username>","password":"<your-password>"}' https://gentle-stream-37536.herokuapp.com/
```



### Developing information

Built with Python/[FastAPI](https://fastapi.tiangolo.com) and Selenium with Chrome Webdriver


> This is my first project with Selenium, feel free to contribute if you find weak code parts or star the project :)

> Alexis Tonneau, UC Berkeley Student
