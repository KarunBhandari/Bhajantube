function handleInputChange(input, labelId) {
    var label = document.getElementById(labelId);
    if (input.value.length > 0) {
      label.style.display = 'none';
    } else {
      label.style.display = 'block';
    }
  }
  