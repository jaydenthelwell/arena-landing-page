document.addEventListener("DOMContentLoaded", function () {
  let currentSlide = 0;
  const totalSlides = 8;
  const nextBtn = document.getElementById("next-btn");
  const backBtn = document.getElementById("back-btn");

  function showNextSlide() {
    //make current slide by invisible
    document.getElementById(`quiz-slide-${currentSlide}`).style.display = "none";
    //increment by 1
    currentSlide++;

    if (currentSlide < totalSlides) {
        //make current slide by visible up to and including last slide
        document.getElementById(`quiz-slide-${currentSlide}`).style.display = "block";
    } else {
        submitQuiz();
    }
  }

  function showPreviousSlide() {
    // make current slide visible
    document.getElementById(`quiz-slide-${currentSlide}`).style.display = "none";
    //decrease by 1
    currentSlide--;

    if (currentSlide >= 0) {
        //make current slide by visible up to and including last slide
        document.getElementById(`quiz-slide-${currentSlide}`).style.display = "block";
    }
  }

  function submitQuiz() {
    console.log("Submitting quiz...")
      const fullName = document.getElementById("full-name").value;
      console.log("Full Name Saved...")
      const phoneNumber = document.getElementById("phone-number").value;
      const gender = document.getElementById("gender").value;
      const genderPreference = document.getElementById("gender-preference").value;
      const ageRange = document.getElementById("age").value;
      const location = document.getElementById("location").value;

      const favouriteSports = [];
      document.querySelectorAll("input[name='favourite_sports']:checked").forEach((input) => {
          if (input.value === "other") {
              const customSport = document.getElementById("custom-sport").value;
              if (customSport) favouriteSports.push(customSport);
          } else {
              favouriteSports.push(input.value);
          }
      });

      const quizData = {
          full_name: fullName,
          phone_number: phoneNumber,
          gender: gender,
          gender_preference: genderPreference,
          age_range: ageRange,
          location: location,
          favourite_sports: favouriteSports,
      };

      fetch("http://127.0.0.1:5001/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(quizData),
    })
    .then((response) => {
        console.log("Raw response object:", response);

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        return response.json(); // parse JSON response
    })
    .then((data) => {
      console.log("Filtered sessions data:", data);
      if (data.sessions && Array.isArray(data.sessions)) {
          console.log("Number of sessions:", data.sessions.length);
          displaySessions(data.sessions);
      } else {
          console.error("No sessions found.");
      }

      alert("Quiz completed successfully!");
  })
    .catch((error) => {
        console.error("Error saving quiz:", error);
    });


    console.log("Quiz Submitted...")
  }

  function displaySessions(sessions) {
    const resultsContainer = document.getElementById("results-container");  // add container for results
    resultsContainer.innerHTML = "";  // clear previous results
    if (sessions.length === 0) {
      resultsContainer.innerHTML = "<p>No sessions available based on your preferences.</p>";
    } else {
      sessions.forEach(session => {
        const sessionDiv = document.createElement("div");
        sessionDiv.classList.add("session");
        sessionDiv.innerHTML = `
          <p>Sport: ${session.sport_name}</p>
          <p>Location: ${session.location}</p>
          <p>Game Size: ${session.game_size}</p>
          <p>Gender preference: ${session.gender}</p>
          <p>Price: £${session.price}</p>
          <p>Slots Remaining: ${session.slots_remaining}</p>
          <p>Date and Time: ${session.date_time}</p>
        `;
        resultsContainer.appendChild(sessionDiv);
      });
    }
  }

  // document.getElementById(`quiz-slide-${currentSlide}`).style.display = "block";
  nextBtn.addEventListener("click", function () {
    //checks is the current slide is not the first
    if (currentSlide > 0) {
      const currentInputs = document.querySelectorAll(`#quiz-slide-${currentSlide} input, #quiz-slide-${currentSlide} select`);
      console.log(currentSlide)
      let isValid = true
      let checkboxTicked = false
      let allFieldsFilled = true

      currentInputs.forEach(input => {
        // if at least one check box is ticked
        if (input.type === "checkbox" && input.checked) {
          checkboxTicked = true;
        }
        console.log("Checkbox status: ", checkboxTicked)
        // if text entered or number entered or option selected
        if ((input.type === "text" || input.type === "tel" || input.tagName === "SELECT") && input.value.trim() === "") {
          allFieldsFilled = false;
        }
        console.log("All fields filled staturs: ", allFieldsFilled)
      });
      if (checkboxTicked || allFieldsFilled) {
        isValid = true;
        showNextSlide();
      } else {
        isValid = false;
        alert("Please complete all fields or select at least one checkbox.");
      }
    } else {

      //  move to next slide if on the first slide (slide 0)
      showNextSlide();
    }

  });

  backBtn.addEventListener("click", function () {
    if (currentSlide > 0) {
      showPreviousSlide();
    }
  });
});
