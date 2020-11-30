$(function () {
    $('.toast').toast('show');

})
var IsAjaxExecuting= false;
var modal = $("#modalHistorico");
$(document).ready(function () {
    $(".modalOpen").on("click", function () {
        if(IsAjaxExecuting) return; // new code
        IsAjaxExecuting = true;
        $.ajax({
            url: $(this).attr("data-url"),
            success: function (data) {
                modal.html(data);
                $("#historicoAluno").modal();
                IsAjaxExecuting = false;
            }
        });
    });
})
