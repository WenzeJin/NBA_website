function isValidFloat(str) {
  return (/^-?[\d]*(\.[\d]+)?$/g).test(str);
}

function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switch_count = 0;
  table = document.getElementById("roster-table");
  console.log(table != null)
  if (table != null) {

    switching = true;
    dir = "asc";

    while (switching) {
      switching = false;
      rows = table.rows;
      console.log(rows)

      for (i = 1; i < (rows.length - 1); i++) {

        shouldSwitch = false;

        x = rows[i].getElementsByTagName("TD")[n];
        y = rows[i + 1].getElementsByTagName("TD")[n];

        x = x.innerHTML;
        y = y.innerHTML;

        if (dir === "asc") {
          if (!isValidFloat(x)) {
            let xWords = x.split(' ')[1];
            let yWords = y.split(' ')[1];
            if (xWords.toLowerCase() > yWords.toLowerCase()) {
              shouldSwitch = true;
              break;

            }
          } else {
            if (parseFloat(x) > parseFloat(y)) {
              shouldSwitch = true;
              break;
            }
          }
        } else if (dir === "desc") {
          if (!isValidFloat(x)) {
            let xWords = x.split(' ')[1];
            let yWords = y.split(' ')[1];
            if (xWords.toLowerCase() < yWords.toLowerCase()) {
              shouldSwitch = true;
              break;
            }
          } else {
            if (parseFloat(x) < parseFloat(y)) {
              shouldSwitch = true;
              break;
            }
          }
        }
      }
      if (shouldSwitch) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        switch_count++;
      } else {
        if (switch_count === 0 && dir === "asc") {
          dir = "desc";
          switching = true;
        }
      }
    }
  } else {
    table = document.getElementById("teams-table");
      switching = true;
    dir = "asc";

    while (switching) {
      switching = false;
      rows = table.rows;

      for (i = 1; i < (rows.length - 1); i++) {

        shouldSwitch = false;

        x = rows[i].getElementsByTagName("TD")[n];
        y = rows[i + 1].getElementsByTagName("TD")[n];

        x = x.innerHTML;
        y = y.innerHTML;
        if (x.startsWith("<a")) {
          x = rows[i].getElementsByTagName("TD")[n].textContent;
          // x = document.getElementById("a-team").textContent
        }
        console.log(x)

        if (y.startsWith("<a")) {
          y = rows[i+1].getElementsByTagName("TD")[n].textContent;
          // y = document.getElementById("a-team").textContent
        }
        console.log(y)

        if (dir === "asc") {
          if (!isValidFloat(x)) {
            // let xWords = x.split(' ')[0];
            // let yWords = y.split(' ')[0];
            // console.log(xWords)
            if (x.toLowerCase() > y.toLowerCase()) {
              shouldSwitch = true;
              break;

            }
          } else {
            if (parseFloat(x) > parseFloat(y)) {
              shouldSwitch = true;
              break;
            }
          }
        } else if (dir === "desc") {
          if (!isValidFloat(x)) {
            // let xWords = x.split(' ')[0];
            // let yWords = y.split(' ')[0];
            // console.log(xWords)
            if (x.toLowerCase() < y.toLowerCase()) {
              shouldSwitch = true;
              break;
            }
          } else {
            if (parseFloat(x) < parseFloat(y)) {
              shouldSwitch = true;
              break;
            }
          }
        }
      }
      if (shouldSwitch) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        switch_count++;
      } else {
        if (switch_count === 0 && dir === "asc") {
          dir = "desc";
          switching = true;
        }
      }
    }
  }
  console.log("ZAKONCZONE")
}