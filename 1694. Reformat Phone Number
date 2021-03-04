var reformatNumber = function (number) {
  numArray = [...number];
  newArray = [];
  for (i = 0; i < numArray.length; i++) {
    if (numArray[i] === " " || numArray[i] === "-") {
      continue;
    } else {
      newArray.push(numArray[i]);
    }
  }
  console.log("numy", numArray);
  console.log("nw", newArray);
  ans = "";
  function blockFormation(num, newArray) {
    res = "";
    for (i = 0; i < num; i++) {
      digit = newArray.pop();
      res = digit + res;
    }
    return res;
  }
  function dashing(stringy) {
    return "-" + stringy;
  }
  n = newArray.length;
  switch (n % 3) {
    case 1:
      ans = blockFormation(2, newArray);
      if (newArray.length > 0) {
        ans = dashing(ans);
      }
      ans = blockFormation(2, newArray) + ans;
      if (newArray.length > 0) {
        ans = dashing(ans);
      }
      while (newArray.length > 0) {
        ans = blockFormation(3, newArray) + ans;
        if (newArray.length > 0) {
          ans = dashing(ans);
        } else {
          break;
        }
      }
      console.log(newArray);
      break;
    case 2:
      ans = blockFormation(2, newArray);
      if (newArray.length > 0) {
        ans = dashing(ans);
      }
      while (newArray.length > 0) {
        ans = blockFormation(3, newArray) + ans;
        if (newArray.length > 0) {
          ans = dashing(ans);
        } else {
          break;
        }
      }
      break;
    case 0:
      console.log(newArray);
      while (newArray.length > 0) {
        console.log("ans", ans);
        ans = blockFormation(3, newArray) + ans;
        if (newArray.length > 0) {
          console.log("b4dashing", ans);
          ans = dashing(ans);
        } else {
          break;
        }
      }
      break;
  }
  return ans;
};
