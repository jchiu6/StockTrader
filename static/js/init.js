$(function() {
        $('#loadingspin').hide();
        $('#hovering').hide();
        var totalPoints = 24, updateInterval = 5000; //milliseconds
        var now1 = new Date().getTime(), now2 = new Date().getTime(), now3 = new Date().getTime(), now4 = new Date().getTime();
        var dataPy1,dataPy2,dataPy3, dataPy4, prevVal1, prevVal2, prevVal3, prevVal4, AImoney, AIstock1, AIstock2, AIstock3, AIstock4, AIWin, PlayerWinJS = "", currentTime, myVar;
        var data1 = [], data2 = [], data3 = [], data4 = [];

        function pushGraph1() {
            if (data1.length > 0)
            data1.shift();
            while(data1.length < totalPoints) {
                var y = dataPy1;
                var temp = [now1 += updateInterval, y];
                data1.push(temp);
             }
            return data1;
        }

        function pushGraph2() {
            if (data2.length > 0)
            data2.shift();
            while(data2.length < totalPoints) {
                var y = dataPy2;
                var temp = [now2 += updateInterval, y];
                data2.push(temp);
            }
            return data2;
        }

        function pushGraph3() {
            if (data3.length > 0)
            data3.shift();
            while(data3.length < totalPoints) {
                var y = dataPy3;
                var temp = [now3 += updateInterval, y];
                data3.push(temp);
            }
            return data3;
        }

        function pushGraph4() {
            if (data4.length > 0)
            data4.shift();
            while(data4.length < totalPoints) {
                var y = dataPy4;
                var temp = [now4 += updateInterval, y];
                data4.push(temp);
            }
            return data4;
        }
        
        var plot1 = $.plot("#placeholder1", [pushGraph1()] , {
            series: {
                shadowSize: 0,  // Drawing is faster without shadows
                color: 'rgba(128,203,196, 1.0)',
                lines: {
                    show: true,
                    lineWidth: 1.2,
                    fill: true,
                    fillColor: 'rgba(128,203,196, 0.6)'
                }
            },
            yaxis: {
                min: 0,
                max: 100
            },
            xaxis: {
                    mode: "time",
                    tickSize: [30, "second"],
                    tickFormatter: function (v, axis) {
                        var date = new Date(v);

                        if (date.getSeconds() % 60 == 0) {
                            var hours = date.getHours() < 10 ? "0" + date.getHours() : date.getHours();
                            var minutes = date.getMinutes() < 10 ? "0" + date.getMinutes()-2 : date.getMinutes()-2;
                            var seconds = date.getSeconds() < 10 ? "0" + date.getSeconds(): date.getSeconds();

                            return hours + ":" + minutes + ":" + seconds;
                        } else {
                            return "";
                        }
                    },
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 10,
                axisLabelFontFamily: 'Verdana, Arial',
            },
            legend: {
                labelBoxBorderColor: "#fff"
            }
        });

        var plot2 = $.plot("#placeholder2", [ pushGraph2() ], {
            series: {
                shadowSize: 0,  // Drawing is faster without shadows
                color:  'rgba(79,195,247,1.0)',
                lines: {
                    show: true,
                    lineWidth: 1.2,
                    fill: true,
                    fillColor: 'rgba(79,195,247,0.6)'
                }
            },
            yaxis: {
                min: 0,
                max: 1000
            },
            xaxis: {
                mode: "time",
                    tickSize: [30, "second"],
                    tickFormatter: function (v, axis) {
                        var date = new Date(v);

                        if (date.getSeconds() % 60 == 0) {
                            var hours = date.getHours() < 10 ? "0" + date.getHours() : date.getHours();
                            var minutes = date.getMinutes() < 10 ? "0" + date.getMinutes()-2 : date.getMinutes()-2;
                            var seconds = date.getSeconds() < 10 ? "0" + date.getSeconds(): date.getSeconds();
                            
                            return hours + ":" + minutes + ":" + seconds;
                        } else {
                            return "";
                        }
                    },
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 10,
                axisLabelFontFamily: 'Verdana, Arial',
            }
        });
        
        var plot3 = $.plot("#placeholder3", [ pushGraph3() ], {
            series: {
                shadowSize: 0,  // Drawing is faster without shadows
                color: 'rgba(129,199,132,1.0)',
                lines: {
                    show: true,
                    lineWidth: 1.2,
                    fill: true,
                    fillcolor: 'rgba(129,199,132,0.6)',
                }
            },
            yaxis: {
                min: 0,
                max: 10000
            },
            xaxis: {
                mode: "time",
                    tickSize: [30, "second"],
                    tickFormatter: function (v, axis) {
                        var date = new Date(v);

                        if (date.getSeconds() % 60 == 0) {
                            var hours = date.getHours() < 10 ? "0" + date.getHours() : date.getHours();
                            var minutes = date.getMinutes() < 10 ? "0" + date.getMinutes()-2 : date.getMinutes()-2;
                            var seconds = date.getSeconds() < 10 ? "0" + date.getSeconds(): date.getSeconds();

                            return hours + ":" + minutes + ":" + seconds;
                        } else {
                            return "";
                        }
                    },
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 10,
                axisLabelFontFamily: 'Verdana, Arial',
            }
        });
        $(document).ready(function(){
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.modal-trigger').leanModal();
              $('.dropdown-button btn').dropdown({
      inDuration: 300,
      outDuration: 225,
      constrain_width: false, // Does not change width of dropdown to that of the activator
      hover: false, // Activate on click
      alignment: 'left', // Aligns dropdown to left or right edge (works with constrain_width)
      gutter: 0, // Spacing from edge
      belowOrigin: false // Displays dropdown below the button
    }
  );
  });
        
        var plot4 = $.plot("#placeholder4", [ pushGraph4() ], {
            series: {
                shadowSize: 0,  // Drawing is faster without shadows
                lines: {
                    show: true,
                    lineWidth: 1.2,
                    fill: true
                } 
            },
            yaxis: {
                min: 0,
                max: 100000
            },
            xaxis: {
                mode: "time",
                    tickSize: [30, "second"],
                    tickFormatter: function (v, axis) {
                        var date = new Date(v);

                        if (date.getSeconds() % 60 == 0) {
                            var hours = date.getHours() < 10 ? "0" + date.getHours() : date.getHours();
                            var minutes = date.getMinutes() < 10 ? "0" + date.getMinutes()-2 : date.getMinutes()-2;
                            var seconds = date.getSeconds() < 10 ? "0" + date.getSeconds(): date.getSeconds();

                            return hours + ":" + minutes + ":" + seconds;
                        } else {
                            return "";
                        }
                    },
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 10,
                axisLabelFontFamily: 'Verdana, Arial',
            }
        });
        function update() {
            prevVal1 = dataPy1;
            prevVal2 = dataPy2;
            prevVal3 = dataPy3;
            prevVal4 = dataPy4;
            $(function() {
                $.ajax({
                    type: 'GET',
                    url: '/StockTrader/default/graphJson.json',
                    success: function(data) {
                    $('#loadingDivStock').hide();
                    dataPy1 = data.g1y;
                    dataPy2 = data.g2y;
                    dataPy3 = data.g3y;
                    dataPy4 = data.g4y;

                    prevVal1 = dataPy1 - prevVal1;
                    prevVal2 = dataPy2 - prevVal2;
                    prevVal3 = dataPy3 - prevVal3;
                    prevVal4 = dataPy4 - prevVal4;

                    if(prevVal1>0) document.querySelector('.stock1').innerHTML ="Stock 1: $"+dataPy1+" "+"<span style=\"color:#00695c\">"+"+"+prevVal1+"</span>";
                    else if(prevVal1<0) document.querySelector('.stock1').innerHTML ="Stock 1: $"+dataPy1 +" " + "<span style=\"color:#ef5350\">" + prevVal1 + "</span>";
                    else if (prevVal1==0) document.querySelector('.stock1').innerHTML ="Stock 1: $"+dataPy1 + " " + "<span style=\"color:#64b5f6\">" + prevVal1 + "</span>";
                    else document.querySelector('.stock1').innerHTML ="Stock 1: $"+dataPy1;
                    if (prevVal2>0) document.querySelector('.stock2').innerHTML ="Stock 2: $"+dataPy2+"   "+"<span style=\"color:#00695c\">"+"+"+prevVal2+"</span>";
                    else if (prevVal2 < 0) document.querySelector('.stock2').innerHTML ="Stock 2: $"+dataPy2 + "   " + "<span style=\"color:#ef5350\">" + prevVal2 + "</span>";
                    else if (prevVal2 == 0) document.querySelector('.stock2').innerHTML ="Stock 2: $"+dataPy2 + "   " + "<span style=\"color:#64b5f6\">" + prevVal2 + "</span>";
                    else document.querySelector('.stock2').innerHTML ="Stock 2: $"+dataPy2;
                    if (prevVal3 > 0) document.querySelector('.stock3').innerHTML ="Stock 3: $"+dataPy3+"   "+"<span style=\"color:#00695c\">"+"+"+prevVal3+"</span>";
                    else if (prevVal3 < 0) document.querySelector('.stock3').innerHTML ="Stock 3: $"+dataPy3 + "   " + "<span style=\"color:#ef5350\">" + prevVal3 + "</span>";
                    else if (prevVal3 == 0) document.querySelector('.stock3').innerHTML ="Stock 3: $"+dataPy3 + "   " + "<span style=\"color:#64b5f6\">" + prevVal3 + "</span>";
                    else document.querySelector('.stock3').innerHTML ="Stock 3: $"+dataPy3;
                    if (prevVal4 > 0) document.querySelector('.stock4').innerHTML ="Stock 4: $"+dataPy4+"   "+"<span style=\"color:#00695c\">"+"+"+prevVal4+"</span>";
                    else if (prevVal4 < 0) document.querySelector('.stock4').innerHTML ="Stock 4: $"+dataPy4 + "   " + "<span style=\"color:#ef5350\">" + prevVal4 + "</span>";
                    else if (prevVal4 == 0) document.querySelector('.stock4').innerHTML ="Stock 4: $"+dataPy4 + "   " + "<span style=\"color:#64b5f6\">" + prevVal4 + "</span>";
                    else document.querySelector('.stock4').innerHTML ="Stock 4: $"+dataPy4;

                    }
                });
            });
            $(function() {
                $.ajax({
                    type: 'GET',
                    url: '/StockTrader/default/opponentAI.json',
                    success: function(data) {
                    $('#loadingDivAI').hide();
                        
                        AImoney = data.AI_money;
                        AIstock1 = data.AI_stock1;
                        AIstock2 = data.AI_stock2;
                        AIstock3 = data.AI_stock3;
                        AIstock4 = data.AI_stock4;
                        AIWin = data.AIWin;

                        document.querySelector('.AImoney').innerHTML ="Current Money: $"+AImoney;
                        document.querySelector('.AIstock1').innerHTML ="Shares of Stock 1: "+AIstock1;
                        document.querySelector('.AIstock2').innerHTML ="Shares of Stock 2: "+AIstock2;
                        document.querySelector('.AIstock3').innerHTML ="Shares of Stock 3: "+AIstock3;
                        document.querySelector('.AIstock4').innerHTML ="Shares of Stock 4: "+AIstock4;
                        document.querySelector('.AIWin').innerHTML = AIWin;
                        if(AIWin == "AI has won!") {
                            clearTimeout(myVar);
                            $('#modalAI').openModal();
                        }
                        if("{{=PlayerWin}}" == "Player has won!") {
                            clearTimeout(myVar);
                            $('#modalPlayer').openModal();
                            console.log("HELLO WINNER");
                        }
                    }
                });
            });

            plot1.setData([pushGraph1()]);
            plot2.setData([pushGraph2()]);
            plot3.setData([pushGraph3()]);
            plot4.setData([pushGraph4()]);

            plot1.setupGrid()
            plot2.setupGrid()
            plot3.setupGrid()
            plot4.setupGrid()

            plot1.draw();
            plot2.draw();
            plot3.draw();
            plot4.draw();
            var inSeconds = updateInterval/1000;
            function speedUp(){
                updateInterval = updateInterval + 1000;
            }
            function slowDown(){
                updateInterval = updateInterval - 1000;
            }
            document.querySelector('.speed').innerHTML =inSeconds+" seconds between each update";
            myVar = setTimeout(update, updateInterval);
        }
        update();
        function updateTime() {
                                var date = new Date();

                        if (date.getSeconds() % 1 == 0) {
                            var hours = date.getHours() < 10 ? "0" + date.getHours() : date.getHours();
                            var minutes = date.getMinutes() < 10 ? "0" + date.getMinutes(): date.getMinutes();
                            var seconds = date.getSeconds() < 10 ? "0" + date.getSeconds(): date.getSeconds();
                    document.querySelector('.currentTimePST').innerHTML=hours + ":" + minutes + ":" + seconds;}
            setTimeout(updateTime, 1000);
        }
        updateTime();
    });
