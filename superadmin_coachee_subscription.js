/*
 # Copyright 2012-20 IOP Technologies LLP. All Rights reserved.
 # Notice: Your use, modification or distribution of it requires the prior written permission of
 # IOP Technologies LLP
 #
 # Filename: js/sports
 #
 # Version        Date modified        Author        Description of change#
 # --------      -------------        ----------    -------------------------
 # 1.0             March 9, 2020        Suprit       Fresh Development
 */



$(document).ready(function () {
    getAllCoacheeList();
});


function getAllCoacheeList() {

    $.ajax({
        type: "POST",
        url: "/get_all_coachee_list/",
        async: true,
        success: function (data) {

            if (data.result == "success") {

                /*console.log(data.dataList);*/

                $('#coachee_list_subscrip > tbody').empty();

                for (var i = 0; i < data.dataList.length; i++) {

                    var row = '<tr>\n' +
                        '<td>\n' +
                        '<div class="form-check">\n' +
                        '<label class="form-check-label">\n' +
                        '<input class="form-check-input coachee_check" type="checkbox" name="coachee_check" value="" id=' + data.dataList[i].user_code + '>\n' +
                        '<span class="form-check-sign">\n' +
                        '<span class="check"></span>\n' +
                        '</span>\n' +
                        '</label>\n' +
                        '</div>\n' +
                        '</td>\n' +
                        '<td>\n' +
                        '<p class="title coachee_name">' + data.dataList[i].coachee_name + '</p>\n' +
                        '<p class="text-muted"> Age : ' + data.dataList[i].coachee_age + " | Gender : " + data.dataList[i].coachee_gender + '</p>\n' +
                        '</td>\n' +
                        "</tr>";

                    $('#coachee_list_subscrip > tbody').append(row);
                }


            } else if (data.result == "failed") {
                swal(data.msg);
            } else if (data.result == "error") {
                swal(data.msg);
            }
        },
        error: function (error) {
            swal("Internal Server error. Please try after sometimes.");
        }
    });
}