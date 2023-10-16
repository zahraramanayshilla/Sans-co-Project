function sign_in() {
    let username = $("#input-username").val();
    let password = $("#input-password").val();
    if (!username || !password) {
        alert("Mohon lengkapi username dan password.");
        return;
    }

    $.ajax({
        type: "POST",
        url: "/login_save",
        data: {
            username_login: username,
            password_login: password,
        },
        success: function (response) {
            if (response["result"] === "success") {
                let token = response["token"];
                $.cookie("mytoken", token, { path: "/" });
                alert("Login Berhasil!");
                window.location.href = "/adminm";
            } else {
                alert(response["msg"]);
            }
        },        
    });
}