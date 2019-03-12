$('#myModal').on('show.bs.modal', function (e) {
    let link = $(e.relatedTarget);
    $(this).find(".modal-body").load(link.attr("href"));
});
