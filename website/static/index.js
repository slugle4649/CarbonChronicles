let once = true;
let single = true

function click(event){
    let target = event.target;
    if( target.querySelector("title") == null ){
        target = target.parentNode;
    }
    let name = target.querySelector("title");
    
    console.log('help')
    once = false
    

    fetch('http://127.0.0.1:5000/click_information', {
        method: 'POST',
        body: JSON.stringify({
            'country' : name.textContent
        }),
        headers: {
        'Content-type': 'application/json; charset=UTF-8',
        }
        }).then(response => response.json()).then(
            response => redirect(response))
}

function hover(event){
    let info = document.getElementById('hoverbar')

    let target = event.target;
    if( target.querySelector("title") == null ){
        target = target.parentNode;
    }
    let name = target.querySelector("title");
        setTimeout(function(){
            info.style.visibility = 'visible'

            if (single == true){

            

            fetch('http://127.0.0.1:5000/hover_information', {
                method: 'POST',
                body: JSON.stringify({
                    'country' : name.textContent
                }),
                headers: {
                'Content-type': 'application/json; charset=UTF-8',
                }
                }).then(response => response.json()).then(
                    response => change_hover(response, name.textContent))

                single =false
                }

            }, 1500);
            
    }
    
function change_hover(data, countryname){
    let info = document.getElementById('hoverbar')
    if (data.CO2 == 'No data'){
        info.textContent = 'Sorry, we dont have data for this country'
    }
    else{
        info.textContent = countryname + 's CO2 emissions in metric tons is ' + data.CO2 + ', which is ' + data.Ranking + ' worldwide'
    }
}

function unhover(event){
    let info = document.getElementById('hoverbar')
    info.style.visibility = 'hidden'
    once = true
    single = true
}

function redirect(data){
    let redirecturl = ''
    for (let key in data){
        redirecturl += key + '=' + data[key] + '&'
    }
    window.location.href = "http://127.0.0.1:5000/detailed_information?" + redirecturl;
}

function init(){
    let countries = document.querySelectorAll(".landxx")
    for(let country of countries){
        country.addEventListener('click', click);
        country.addEventListener('mouseover', hover)
        country.addEventListener('mouseout', unhover);
    }
}


window.onload = init;