function handleDelete(url){
    const userConfirmation = confirm("confirm to delete record");
    if(userConfirmation){
        window.location.href=url;
    }
    else{
        alert("you canceled the deleting");
    }
}
function handleEdit(url){
    window.location.href=url;
}

function handleAdd(url){
    window.location.href=url;
}
