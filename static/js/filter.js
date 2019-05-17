$(document).ready(function() {
    $('#filter-btn').on('click', function(e) {
        console.log('Filter button clicked')
        e.preventDefault();
        var bath_min = $('#bath_min').val();
        var bath_max = $('#bath_max').val();
        var bed_min = $('#bed_min').val();
        var bed_max = $('#bed_max').val();
        $.ajax({
            url:'/estate/bathrooms?bath_min=' + bath_min + '&bath_max=' + bath_max + '&bed_min=' + bed_min + '&bed_max=' + bed_max,
            type: 'GET',
            success: function(resp) {
                var newHTML = resp.data.map(d => {
                    return `<div class="gg">
                                <div class="thumbnail">
                                    <div class="imagelist" id="estateimg">
                                        <img src="${'../media/'}${d.image}" id="img-pic" alt="EstateLogo"/>
                                    </div>
                            
                                    <div class="caption" id="estatebox">
                                        <h3 class="address-single">${d.address}</h3>
                                        <h6>${d.city}, ${d.zip}</h6>
                                        <div><h5> Price:${d.price} ISK</h5></div>
                                        <div class="limit" >
                                            <p>${d.desc}</p>
                                        </div>
                                        <div id="limit_"></div>
                                        <button class="btn btn_seemore" onclick="window.location.href = ${d.id};" id="dropdown-choice">Learn more</button>
                                    </div>
                                </div>
                            </div>`

                });
                $('#flex-box').html(newHTML.join(''));
                $('#bath_min').val('');
                $('#bath_max').val('');
                $('#bed_min').val('');
                $('#bed_max').val('');
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        })
    })
});