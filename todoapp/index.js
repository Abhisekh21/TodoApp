var sbutton = document.getElementById('submit');


async function fetchpost() {
    const response = await fetch('http://127.0.0.1:8000/todos');
    const listofitems= await Response.json()
    return listofitems
}
async function createpost(item) {
    let itemid = Math.random();
    let data = {
        id: itemid,
        value: item

    }
    const response=await fetch('http://127.0.0.1:8000/todos/create',{
        method:"post",
        body: JSON.stringify(data)
    });
    return response.json()

}

function inputhandler() {
    var input = document.getElementById('input');
    if (input.value === '') {
        alert("enter the input filed");
        return
    }
    createpost(input.value)
    reloadul(tasks=fetchpost);
    input.value = '';
};

function deletehandler(index) {
    console.log(`${index}`);
    tasks.splice(index, 1);
    reloadul();
};
function updatehandler(index) {
    var updatetask = prompt('update task:', tasks[index]);
    if (updatetask !== null && updatetask.trim() !== '') {
        tasks[index] = updatetask;
        reloadul();
    }
};
function reloadul(tasks) {
    var itemlist = document.getElementById('item-list');
    itemlist.innerHTML = '';

    for (var index = 0; index < tasks.length; index++) {

        var task = tasks[index];
        var newtask = document.createElement('li');
        newtask.innerText = task;
        var deleteButton = document.createElement('button');
        deleteButton.innerText = 'Delete';
        // deleteButton.onclick = (function (index) {
        //     return function () {
        //         deletehandler(index);
        //     };
        // })(index);
        deleteButton.onclick = function (index) {
            return deletehandler(index);
        }

        var updateButton = document.createElement('button');
        updateButton.innerText = 'Update';
        // updateButton.onclick = (function (index) {
        //     return function () {
        //         updatehandler(index);
        //     };
        // })(index);
        updateButton.onclick = function (index) {
            return updatehandler(index);
        }

        newtask.appendChild(deleteButton);
        newtask.appendChild(updateButton);
        itemlist.appendChild(newtask);
    }
};

// event listners
sbutton.addEventListener('click', inputhandler);