const socket = io("http://localhost:5000");

socket.on("connect", () => {
    // either with send()
    socket.send("Hello!");
    console.log("Connected")

    let form = document.getElementById("form")

    form.addEventListener("submit", (ev) => {
        ev.preventDefault()
        let message = document.getElementById("message")
        console.log(message.value.length)
        if (message.value.length != 0) {
            console.log(`The message is : ${message.value}`)
            socket.emit("sendMessage", message.value)
        }
    })

    // or with emit() and custom event names
    //socket.emit("salutations", ["Hello!", { "mr": "john" }, Uint8Array.from([1, 2, 3, 4])]);
});

socket.on("getMessages", data => {
    console.log(data);
    let messagesDiv = document.getElementById("messages")
    data.forEach(message => {
        let el = document.createElement("div")
        el.className = "message"
        el.innerHTML = message
        messagesDiv.appendChild(el)
    });
});

// handle the event sent with socket.emit()
// socket.on("greetings", (elem1, elem2, elem3) => {
//     console.log(elem1, elem2, elem3);
// });