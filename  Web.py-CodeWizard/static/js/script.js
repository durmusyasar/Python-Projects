$(document).ready(function(){
    console.log("loaded");
    $.material.ini();
    $(document).on("submit", "register-form", function(e){
        e.preventDefault();
        console.log("form submitted");
        var form = $('register-form').serialize();
        $.ajax({
            url: '/postregistration',
            type: 'POST',
            data: form,
            success: function(response){
                console.log(response);
            }
        });
    });
    $(document).on('submit', '#login-form', function(e){
        e.proventDefault();
        var form = $(this).serialize();
        $.ajax({
            url: 'check-login',
            type: 'POST',
            data: form,
            success: function(res){
                if(res == "error"){
                    alert("Could not log in");
                }
                else {
                    console.log("Logged in as", res);
                    window.location.href = "/";
                }
            }
        })
    });
    $(document).on('submit', '#login-form', function(e){
        e.proventDefault();
        var form = $(this).serialize();
        $.ajax({
            url: 'logout',
            type: 'POST',
            success: function(res){
                if(res == "sucsess"){
                    window.location.href = "/login";
                }
                else {
                    alert("Something went wrong.")
                }
            }
        })
    });
    $(document).on('submit', '#post-activity', function(e){
        e.proventDefault();
        var form = $(this).serialize();
        $.ajax({
            url: 'post-activity',
            type: 'POST',
            data: form,
            success: function(res){
                console.log(res);
            }
        })
    });
    $(document).on('submit', '#settings-form', function(e){
        e.proventDefault();
        var form = $(this).serialize();
        $.ajax({
            url: 'update-settings',
            type: 'POST',
            data: form,
            success: function(res){
                if(res == "sucsess"){
                    window.location.href = window.location.href;
                }
                else {
                    alert(res)
                }
            }
        })
    });
    $(document).on('submit', '#.comment-form', function(e){
        e.proventDefault();
        var form = $(this).serialize();
        $.ajax({
            url: 'update-settings',
            type: 'POST',
            data: form,
            success: function(res){
                console.log(res);
            }
        })
    });
});