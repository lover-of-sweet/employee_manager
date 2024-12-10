const csrftoken = Cookies.get('csrftoken')

document.addEventListener("DOMContentLoaded", (event) => 
{
    
    document.getElementById('add').addEventListener('click', function(e) {

        const url = '/manager/add_position/'
        var option = {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin'
    }

        e.preventDefault();

        var post = document.getElementById("position-name").value;
        var categ = document.getElementById("position-category").value;

        var formData = new FormData();
        formData.append('post', post);
        formData.append('category', categ);
        option['body'] = formData;

        fetch(url, option)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            if (data['status'] === 'ok') {
                position()
            }
        })
    })
})
