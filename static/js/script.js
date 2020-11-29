$(function () {
    $('.toast').toast('show');

})

var modal = $("#modalHistorico");

$(".modalOpen").on("click", function () {
    $.ajax({
        url: $(this).attr("data-url"),
        success: function (data) {
            modal.html(data);
            $("#historicoAluno").modal();
        }
    });
});