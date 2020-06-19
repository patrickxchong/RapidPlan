const Storage = Capacitor.Plugins.Storage;

async function getItem(key) {
  let { value } = await Storage.get({ key })
  return value;
}

async function setItem(key, value) {
  return await Storage.set({ key, value });
}

function filter(text, searchString) {
  const regexStr = "(?=.*" + searchString.split(/\,|\s/).join(")(?=.*") + ")";
  const searchRegEx = new RegExp(regexStr, "gi");
  return text.match(searchRegEx) !== null;
}

let itemsArray = [];

(async function onload() {
  let items = await getItem("items")
  itemsArray = items
    ? await JSON.parse(items)
    : [];
  updateCards();
})()


async function submit(e) {
  e.preventDefault();
  await submitHandler();
}

async function submitHandler() {
  let from = document.getElementById("from").value;
  let to = document.getElementById("to").value;
  if (to == "" || from == "") {
    alert("You missed a field!");
    return PromiseRejectionEvent();
  }

  try {
    for (const [key, value] of Object.entries(data)) {
      if (filter(value["name"], from)) {
        from = key;
        break;
      }
    }
    for (const [key, value] of Object.entries(data)) {
      if (filter(value["name"], to)) {
        to = key;
        break;
      }
    }
    if (to.length > 5) {
      throw `${to} Location not found :(`;
    }
    if (from.length > 5) {
      throw `${from} not found :(`;
    }

    itemsArray.unshift({ to, from });
    if (itemsArray.length > 9) {
      itemsArray.pop();
    }
    await setItem("items", JSON.stringify(itemsArray));

    updateCards();
  } catch (e) {
    document.getElementById("app").innerHTML = `
      <p>Something wrong happened!</p>
      <p>${e}</p>`;
    throw e;
  }
}

let form = document.getElementsByTagName("form")[0];

// attach event listener
form.addEventListener("submit", submit, true);


function updateCards() {
  let color = [
    "card--normal",
    "card--water",
    "card--electric",
    "card--fire",
    "card--psychic",
    "card--dark",
    "card--grass",
    "card--ice",
    "card--fairy"
  ];
  document.getElementById("app").innerHTML = `
    <section>
      ${itemsArray
      .map((item, idx) => {
        let trip;
        if (item["from"] < item["to"]) {
          trip = data[item["from"]][item["to"]];
        } else {
          trip = data[item["to"]][item["from"]];
        }
        return `
        <figure class="card ${color[idx]}">
        <figcaption class="card__caption">
          <h1 class="card__name">

          ${item["from"] + ": " + data[item["from"]]["name"]}
          </h1>
          <h1 class="card__name">
          - 
          </h1>
          <h1 class="card__name">
          ${item["to"] + ": " + data[item["to"]]["name"]}
          </h1>
          ${
          trip["duration"]
            ? `<h3 class="card__type">
            ${trip["duration"]} mins
          </h3>`
            : ""
          }
          
          <table class="card__stats">
            <tbody><tr>
              <th>Cashless</th>
              <td>RM ${trip["fares"]["cashless"]}</td>
            </tr>
            <tr>
              <th>Monthly</th>
              <td>RM ${trip["fares"]["monthly"]}</td>
            </tr>
            
            <tr>
              <th>Weekly</th>
              <td>RM ${trip["fares"]["weekly"]}</td>
            </tr>
      
            <tr>
              <th>Cash</th>
              <td>RM ${trip["fares"]["cash"]}</td>
            </tr>
            <tr>
              <th>Concession</th>
              <td>RM ${trip["fares"]["consession"]}</td>
            </tr>
          </tbody></table>
        </figcaption>
      </figure>
          `;
      })
      .join("")}
    </section>
    `;
}
