for (const starRating of document.getElementsByClassName("star-rating")) {
    starRating.addEventListener("keydown", (e) => {
      let action;
      if (e.key === "ArrowRight" || e.key === "ArrowDown") {
        action = "next";
      } else if (e.key === "ArrowLeft" || e.key === "ArrowUp") {
        action = "previous";
      } else {
        return;
      }
  
      e.preventDefault();
  
      const inputs = Array.from(starRating.querySelectorAll("input"));
  
      for (let i = 0; i < inputs.length; i++) {
        if (document.activeElement === inputs[i]) {
          // focus the next/previous element, since we have reversed the order of the elements we need to subtract on next and add on previous
          let focusToIndex = action === "next" ? i - 1 : i + 1;
          if (focusToIndex < 0) focusToIndex = inputs.length - 1;
          if (focusToIndex >= inputs.length) focusToIndex = 0;
  
          inputs[focusToIndex].focus();
          inputs[focusToIndex].checked = true;
          break;
        }
      }
    });
  }