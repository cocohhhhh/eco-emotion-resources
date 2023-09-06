$(document).ready(function () {
    var margin = $('.bubble.smaller').height()/2;
    // Iterate over each 'bubble' class
    $('.bubble').each(function () {
        var bubble = $(this);
        
        // Find all elements with both classes 'bubble' and 'smaller' inside the current 'bubble'
        var smallerList = bubble.find('.bubble.smaller');
        var N = smallerList.length;
        var R = (bubble.height() / 2 ) -margin; // Adjust this based on your desired positioning logic

        // Iterate over 'smaller bubble' elements within the current 'bubble'
        smallerList.each(function (index) {
            var smallerBubble = $(this);

            // Set the position of the smaller bubble
            // You can modify this part to set the position as needed
            var positionX = R * Math.cos((2 * Math.PI * index) / N + Math.PI/2); // Adjust this based on your desired positioning logic
            var positionY = -R * Math.sin((2 * Math.PI * index) / N + Math.PI/2); // Adjust this based on your desired positioning logic
            smallerBubble.css({
                transform: 'translate(' + positionX + 'px, ' + positionY + 'px)'
            });
        });
    });
});
