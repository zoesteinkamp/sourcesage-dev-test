/**
 * Created by zoesteinkamp on 5/18/15.
 */
swampdragon.ready(function () {
    var myVar = document.getElementById("myVar").value;
    swampdragon.open(function() {
        // Subscribing to all channels provided by locationcurrent-router
        swampdragon.subscribe('answer', 'swampy-channel', null, function (context, data) {
            this.dataMapper = new DataMapper(data);
            console.log("we are subscribed")
        }, function (context, data) {
            console.log("Failure to subscribe")
        });

        swampdragon.getList('answer', {}, function (context, data) {
             data.forEach(function (item) {
                 if(item.answer == myVar ){
                    var rootdown = document.getElementById("answers");
                    var para = document.createElement("p");
                    var newest = document.createTextNode(item.post);
                    para.appendChild(newest);
                    var header = document.createElement("h4");
                    var head = document.createTextNode("Posted by: " + item.answerer);
                    header.appendChild(head);
                    rootdown.appendChild(head);
                    rootdown.appendChild(para);
                 }
             });
        }, function(context, data) {
            console.log("No answers yet")
        });
        swampdragon.onChannelMessage(function (channels, message) {
            var dragonid = message.data.id;
            var post = message.data.post;
            var answerer = message.data.answerer;
            var answer = message.data.answer;
            if (message.action === "created") {
                if(answer == myVar ){
                    var start = rootdown.firstChild;
                    var rootdown = document.getElementById("answers");
                    var para = document.createElement("p");
                    var newest = document.createTextNode(post);
                    para.appendChild(newest);
                    var header = document.createElement("h4");
                    var head = document.createTextNode("Posted by: " + answerer);
                    header.appendChild(head);
                    rootdown.insertBefore(head,start);
                    rootdown.insertBefore(para, start);
                 }
            }
        });
    });
});