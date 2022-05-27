async function makePostRequest(url, data) {
    await fetch(
        url,
        {
            method: "POST",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        },
    ).then(async rawResponse => {
        var content = await rawResponse.text()
        console.log(content);
    });
}

document.getElementById("submit").onclick = function(event) {
    const input = document.getElementById("input")
    const note = input.value
    let url = "/post";
    makePostRequest(url, {"text":note});
    location.reload();
}

for (element of document.getElementsByClassName("remove")){
    element.onclick = (event) => {
    let url = "/remove";
    makePostRequest(url, {"_id":event.srcElement.id});
    location.reload();
}}
