/*$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url:'/estate?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHTML = resp.data.map(d => {
                    return `<div class="thumbnail">
                                <div class="imagelist" id="estateimg">
                                    <img src="${'../media/'}${d.image}" id="img-pic" alt="EstateLogo"/>
                                </div>

                                <div class="caption" id="estatebox">
                                    <h3>${d.address}</h3>
                                    <h4>Price:${d.price} ISK</h4>
                                    <div class="limit">
                                        <p>${d.desc}</p>
                                    </div>
                                    <br>
                                    <button class='btn' onclick="window.location.href = ${d.id};" id="dropdown-choice">Learn more</button>
                                </div>
                            </div>`
                });
                $('#flex-box').html(newHTML.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        })
    })
});*/