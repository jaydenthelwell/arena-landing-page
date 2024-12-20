import random
from datetime import datetime, timedelta
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

sessions = [
    {
        "favourite_sports": "Football",
        "sessions": [
            {"gender": "male", "location": "north-london", "address": "123 North London Rd, London, NW1 1AA", "game_size": "5-a-side", "price": 10, "slots_remaining": 1, "date_time": "2024-12-30 14:00", "age": "18-25"},
            {"gender": "female", "location": "north-london", "address": "123 North London Rd, London, NW1 1AA", "game_size": "5-a-side", "price": 10, "slots_remaining": 5, "date_time": "2024-12-20 18:45", "age": "18-25"},
            {"gender": "male", "location": "north-london", "address": "123 North London Rd, London, NW1 1AA", "game_size": "5-a-side", "price": 10, "slots_remaining": 3, "date_time": "2024-12-29 19:00", "age": "18-25"},
            {"gender": "any", "location": "north-london", "address": "123 North London Rd, London, NW1 1AA", "game_size": "5-a-side", "price": 10, "slots_remaining": 2, "date_time": "2024-12-20 18:15", "age": "26-35"},
            {"gender": "female", "location": "south-london", "address": "456 South London St, London, SE1 2BB", "game_size": "7-a-side", "price": 12, "slots_remaining": 0, "date_time": "2024-12-21 19:00", "age": "26-35"},
            {"gender": "any", "location": "east-london", "address": "789 East London Ave, London, E2 3CC", "game_size": "5-a-side", "price": 8, "slots_remaining": 7, "date_time": "2024-12-22 17:00", "age": "36-45"},
            {"gender": "male", "location": "west-london", "address": "101 West London Rd, London, W3 4DD", "game_size": "11-a-side", "price": 15, "slots_remaining": 10, "date_time": "2024-12-23 14:00", "age": "46-60"},
        ]
    },
    {
        "favourite_sports": "Basketball",
        "sessions": [
            {"gender": "male", "location": "north-london", "address": "123 North London Rd, London, NW1 1AA", "game_size": "5-a-side", "price": 10, "slots_remaining": 5, "date_time": "2024-12-20 19:00", "age": "18-25"},
            {"gender": "female", "location": "south-london", "address": "456 South London St, London, SE1 2BB", "game_size": "5-a-side", "price": 12, "slots_remaining": 3, "date_time": "2024-12-21 18:00", "age": "26-35"},
            {"gender": "any", "location": "east-london", "address": "789 East London Ave, London, E2 3CC", "game_size": "5-a-side", "price": 8, "slots_remaining": 7, "date_time": "2024-12-22 16:00", "age": "36-45"},
            {"gender": "male", "location": "west-london", "address": "101 West London Rd, London, W3 4DD", "game_size": "5-a-side", "price": 15, "slots_remaining": 10, "date_time": "2024-12-23 15:00", "age": "46-60"},
        ]
    },
    {
        "favourite_sports": "Tennis",
        "sessions": [
            {"gender": "any", "location": "north-london", "address": "123 North London Rd, London, NW1 1AA", "game_size": "1v1", "price": 20, "slots_remaining": 0, "date_time": "2024-12-19 12:00", "age": "60-75"},
            {"gender": "male", "location": "south-london", "address": "456 South London St, London, SE1 2BB", "game_size": "1v1", "price": 25, "slots_remaining": 4, "date_time": "2024-12-20 14:00", "age": "18-25"},
            {"gender": "female", "location": "east-london", "address": "789 East London Ave, London, E2 3CC", "game_size": "1v1", "price": 18, "slots_remaining": 2, "date_time": "2024-12-22 13:00", "age": "26-35"},
            {"gender": "any", "location": "north-london", "address": "123 North London Rd, London, NW1 1AA", "game_size": "doubles", "price": 25, "slots_remaining": 0, "date_time": "2024-12-27 12:30", "age": "36-45"},
            {"gender": "male", "location": "south-london", "address": "456 South London St, London, SE1 2BB", "game_size": "doubles", "price": 30, "slots_remaining": 9, "date_time": "2024-12-29 14:30", "age": "46-60"},
            {"gender": "female", "location": "east-london", "address": "789 East London Ave, London, E2 3CC", "game_size": "doubles", "price": 23, "slots_remaining": 4, "date_time": "2024-12-31 13:15", "age": "60-75"},
        ]
    },
    {
        "favourite_sports": "Rugby",
        "sessions": [
            {"gender": "male", "location": "north-london", "address": "123 North London Rd, London, NW1 1AA", "game_size": "7-a-side", "price": 25, "slots_remaining": 8, "date_time": "2024-12-21 16:00", "age": "18-25"},
            {"gender": "male", "location": "south-london", "address": "456 South London St, London, SE1 2BB", "game_size": "7-a-side", "price": 22, "slots_remaining": 4, "date_time": "2024-12-22 17:00", "age": "26-35"},
        ]
    },
    {
        "favourite_sports": "Netball",
        "sessions": [
            {"gender": "female", "location": "north-london", "address": "123 North London Rd, London, NW1 1AA", "game_size": "7-a-side", "price": 10, "slots_remaining": 6, "date_time": "2024-12-20 17:00", "age": "36-45"},
            {"gender": "female", "location": "south-london", "address": "456 South London St, London, SE1 2BB", "game_size": "7-a-side", "price": 12, "slots_remaining": 4, "date_time": "2024-12-21 16:00", "age": "46-60"},
            {"gender": "female", "location": "east-london", "address": "789 East London Ave, London, E2 3CC", "game_size": "7-a-side", "price": 8, "slots_remaining": 8, "date_time": "2024-12-22 15:00", "age": "60-75"},
            {"gender": "female", "location": "west-london", "address": "101 West London Rd, London, W3 4DD", "game_size": "7-a-side", "price": 10, "slots_remaining": 3, "date_time": "2024-12-23 13:00", "age": "75+"},
        ]
    }
]


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            quiz_data = request.json
            print("Quiz Data:", quiz_data)

            # process  results
            age = quiz_data.get('age_range')
            gender = quiz_data.get('gender_preference')
            favourite_sports = quiz_data.get('favourite_sports', [])
            location = quiz_data.get('location')

            current_date = datetime.now()
            filtered_sessions = []

            # filtering the sessions based on answers
            for sport_data in sessions:
                sport_name = sport_data["favourite_sports"]
                print(f"Checking sport: {sport_name} against user's favourite_sports: {favourite_sports}")
                # check if the sport_name is in the list of user's favourite sports

                if sport_name.lower() not in [sport.lower() for sport in favourite_sports]:
                    continue
                for session in sport_data["sessions"]:
                    if gender != "any" and session["gender"] != gender:
                        continue
                    if age != session["age"]:
                        continue
                    if session["location"].lower() != location.lower():
                        continue
                    if sport_name.lower() not in favourite_sports:
                        continue
                    session_date = datetime.strptime(session["date_time"], "%Y-%m-%d %H:%M")
                    if session_date < current_date:
                        continue
                    if session["slots_remaining"] <= 0:
                        continue
                    session_with_sport = session.copy()  # copy session data to avoid changing original data
                    session_with_sport["sport_name"] = sport_name  # Add the sport name to the session data

                    filtered_sessions.append(session_with_sport)
                    print(filtered_sessions)
            # return filtered sessions as a JSON response
            return jsonify({"sessions": filtered_sessions})
        except Exception as e:
            print("Error processing quiz:", e)
            return jsonify({"error": "Something went wrong"}), 500

    # GET request, render home page with the quiz form
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
