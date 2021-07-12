from flask import Flask
from flask import request
import datetime
from datetime import datetime
from datetime import timedelta
import math


#my-first-web-app-319405

app = Flask(__name__)

@app.route("/")
def index():
    running_time = str(request.args.get("running_time", "")).strip()
    running_distance = str(request.args.get("running_distance", "")).strip()
    running_pace = str(request.args.get("running_pace")).strip()
    if running_time and running_distance != "":
        final_output = running_pace_calculator(running_time, running_distance, running_pace)
    elif running_distance and running_pace != "":
        final_output = running_pace_calculator(running_time, running_distance, running_pace)
    elif running_time and running_pace != "":
        final_output = running_pace_calculator(running_time, running_distance, running_pace)
    else:
        final_output = ""
    return (
        """
        <head> <title> Running Calculator </title>
        <style>
		input[type=text] {
  		display: flex;
  		flex-direction: column;
  		font-family: freight-sans-pro;
  		font-size: 25;
  		border: 5px solid #074470;
  		color: rgba(12,12,12, 1);
  		margin-left: 10px;
  		}
  		input[type=datetime] {
  		display: flex;
  		flex-direction: column;
  		font-family: freight-sans-pro;
  		font-size: 25;
  		border: 5px solid #074470;
  		color: rgba(12,12,12, 1);
  		margin-left: 10px;
  		}
  		input[type=submit] {
  		display: flex;
  		flex-direction: column;
  		font-family: freight-sans-pro;
  		font-size: 35;
  		border: 2px solid #074470;
  		color: rgba(12,12,12, 1);
  		}
  		body {
  		background: url('https://i.pinimg.com/originals/04/34/89/043489e7922dabf9902965b964ca04a5.jpg');
  		background-repeat: no-repeat; 
  		background-size: cover; 
  		}
  		h1.basic {
  		font-family: freight-sans-pro, sans-serif;
  		font-weight: 500;font-style: italic;
  		font-size: 60;
  		}
  		p.important {
  		font-family: freight-sans-pro,sans-serif;
  		font-weight: 600;
  		font-style: normal;
  		color: #074470;
  		font-size: 25
  		}
  		p.finaloutput {
  		font-family: freight-sans-pro;
  		font-weight: 600;
  		font-style: normal;
  		color: #074470;
  		font-size: 30;
  		}
  		p.content {
  		font-family: freight-sans-pro,
		sans-serif;
		font-weight: 300;
		font-style: normal;
		color: #074470;
		font-size: 25;
		font-style:bold;
  		}
  		form.main {
  		font-family: freight-sans-pro,sans-serif;
  		font-weight: 300;
  		font-style: normal;
  		color: #074470;
  		font-size: 25;
  		}
		</style>
        <meta name="google-site-verification" content="V8H7aaaQsnfG1eYLO53su1jSljjeWU9JQljkzPUiZ00" />
        <meta name="viewport" content="width=device-width, initial-scale=0.9">
        <link rel="stylesheet" href="https://use.typekit.net/bcc4lnw.css">
        <h1 class = "basic"> Running Pace Calculator </h1>
        <p class = "important"> Enter any two to calculate pace, time or distance. </p>
        <body>
        <form class="main" action="" method="get">
                Running Time: <input type="datetime" name="running_time">
                
                Running Distance (Miles): <input type = "text" name = "running_distance">
                
                Running Pace (Minutes Per Mile): <input type = "text" name = "running_pace"
                <br>
                <br>
                <input type="submit" value="Convert">
            </form>
            </body>
            </head> """
        + f"""<p class="finaloutput"> {final_output} </p>"""
        +
    """
        <p class="important">
        Who Uses a Pace Calculator? </p>
        <p class="content">
        Both new and experienced runners can benefit from pace calculators.
        Knowing your pace can help you train and run better, whether you're
        running your first race, striving to set a personal best, or going for a training run.
         </p>
        <p class="important">
        Why are pace calculators useful? </p>
        <p class="content">
        Pace calculators can help you figure out how quickly you should
        run if you have a specific finish time in mind for a particular distance or race.
        Find out what speed you need to run a 20-minute 5K or a sub-1:30 half marathon, for example.
        <br>
        <br>
        Pace calculators can also be used to figure out what your pace was during a
        training run in the neighborhood or on the track.Find out how quickly you
        ran for that 30-minute 4-mile training run, for example.
        <br>
        <br>
        Finally, they can assist you in determining the distance you ran. For example,
        you may figure out how far you ran by entering your pace and the length of
        your training run or race.
        <p class="important"> Powered by Google Cloud Computing </p>
        """
    )


def running_pace_calculator(running_time, running_distance, running_pace):
    """Convert Running Total Time and Miles Run to Running Pace"""
    time_format = "%H:%M:%S"
    pace_format = "%M:%S"
    try:
        if running_time and running_distance != "":
            try:
                formatted = datetime.strptime(str(running_time), time_format)
                total_seconds = (formatted.hour * 3600) + (
                    formatted.minute * 60) + formatted.second
                pace = total_seconds / float(running_distance)
                m, s = divmod(int(pace), 60)
                return f"{m:2d}:{s:02d}" + " " + "per mile"
            except ValueError:
                running_time = "00:" + running_time
                formatted = datetime.strptime(str(running_time), time_format)
                total_seconds = (formatted.hour * 3600) + (
                    formatted.minute * 60) + formatted.second
                pace = total_seconds / float(running_distance)
                m, s = divmod(int(pace), 60)
                return f"{m:2d}:{s:02d}" + " " + "per mile"
        elif running_distance and running_pace != "":
            formatted = datetime.strptime(str(running_pace), pace_format)
            minutes = (float(formatted.minute) * float(running_distance)) * 60
            seconds = float(formatted.second) * float(running_distance)
            total_seconds = round((minutes + seconds))
            return str(timedelta(seconds=total_seconds))
        elif running_time and running_pace != "":
            try:
                formatted = datetime.strptime(str(running_time), time_format)
                time_seconds = formatted.hour * 3600 + formatted.minute * 60 + formatted.second
                for_pace = datetime.strptime(running_pace, pace_format)
                pace_seconds = for_pace.minute * 60 + for_pace.second
                return str(round(
                    (time_seconds / pace_seconds), 2)) + " " + "miles"
            except ValueError:
                running_time = "00:" + running_time
                formatted = datetime.strptime(str(running_time), time_format)
                time_seconds = formatted.hour * 3600 + formatted.minute * 60 + formatted.second
                for_pace = datetime.strptime(running_pace, pace_format)
                pace_seconds = for_pace.minute * 60 + for_pace.second
                return str(round(
                    (time_seconds / pace_seconds), 2)) + " " + "miles"
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug = True)
