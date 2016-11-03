$(document).ready(function () {
    // Tabbed Content

    $('.tabs li').click(function () {
        // alert("li");
        $(this).closest('.tabs').find('li').removeClass('active');
        $(this).addClass('active');
        var liIndex = $(this).index() + 1;
        $(this).closest('.tabbed-content').find('.father>li').removeClass('active');
        $(this).closest('.tabbed-content').find('.father>li:nth-of-type(' + liIndex + ')').addClass('active');
    });

    $('.nav a').click(function () {
        // alert("nav");
        $(this).closest('.nav').find('a').removeClass('active');
        $(this).addClass('active');
        var liIndex = $(this).index() + 1;
        $(this).closest('.tab-content').find('.child>li').removeClass('active');
        $(this).closest('.tab-content').find('.child>li:nth-of-type(' + liIndex + ')').addClass('active');
    });


    var myChart = echarts.init(document.getElementById('main1'), 'infographic');
    testAjax();

    function testAjax() {
        var aj = $.ajax({
            url: 'echart',// 跳转到 action
            data: {
                //year: $("#search_year").val(),
                //keyword: $("#search_keyword").val()
                type: "1"
            },
            type: 'post',
            cache: false,
            dataType: 'json',
            success: function (data) {
                if (data != null) {
                    //alert(data);
                    myChart.setOption(getOption(data));
                    // window.location.reload();
                } else {
                    view(data.msg);
                }
            },
            error: function () {
                alert("error!!!");
            }
        });
    }


    $("#topic").click(function () {
        if (myChart.getOption() == null) {
            testAjax();
        }
    });

    function getDateFormat(date) {
        var month;
        var day;
        month = (date.getMonth() + 1).toString();
        if (month.length < 2)
            month = '0' + month;
        if (date.getDate().toString().length < 2)
            day = '0' + date.getDate().toString();
        else
            day = date.getDate().toString();
        return date.getFullYear().toString() + '-' + month + '-' + day

    }

    function getOption(data1) {
        var base = +new Date(1990, 1, 1);
        var oneDay = 24 * 3600 * 1000;
        var date = [];
        var today = +new Date();
        var jsonData = data1;
        var compData = [];
        var dayCount = Math.ceil((today - base) / oneDay);
        for (var i = 1; i <= dayCount; i++) {
            var now = new Date(base += oneDay);
            date.push([now.getFullYear(), now.getMonth() + 1, now.getDate()].join('/'));
            var key = getDateFormat(now);
            if (jsonData[key] != null) {
                compData.push(jsonData[key]);
            }
            else
                compData.push(0);
        }
        //console.log('today:' + today);
        //console.log('base:' + base);
        //console.log('dayCount:' + dayCount);
        //console.log('jsonData.length:' + Object.keys(jsonData).length);
        //console.log(jsonData);
        //console.log('date.length:' + date.length);
        //console.log(date);
        //console.log('compData.length:' + compData.length);
        //console.log(compData);

        // 指定图表的配置项和数据
        var option1 = {
            tooltip: {
                trigger: 'axis',
                position: function (pt) {
                    return [pt[0], '10%'];
                }
            },
            title: {
                left: 'center',
                text: '公司上市数量变化图'
            },
            legend: {
                top: 'bottom'
            },
            toolbox: {
                feature: {
                    dataZoom: {
                        yAxisIndex: 'none'
                    },
                    restore: {},
                    saveAsImage: {}
                }
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: date
            },
            yAxis: {
                type: 'value'
            },
            dataZoom: [{
                type: 'inside',
                start: 85,
                end: 100
            }, {
                start: 85,
                end: 100,
                handleIcon: 'M10.7,11.9v-1.3H9.3v1.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4v1.3h1.3v-1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7V23h6.6V24.4z M13.3,19.6H6.7v-1.4h6.6V19.6z',
                handleSize: '80%',
                handleStyle: {
                    color: '#fff',
                    shadowBlur: 3,
                    shadowColor: 'rgba(0, 0, 0, 0.6)',
                    shadowOffsetX: 2,
                    shadowOffsetY: 2
                }
            }
            ],
            series: [
                {
                    name: '上市数量',
                    type: 'line',
                    smooth: true,
                    symbol: 'none',
                    lineStyle: {
                        normal: {
                            color: 'rgb(255, 70, 131)',
                            width: 1.5,
                            shadowColor: 'rgba(255, 70, 131, 0.68)',
                            shadowBlur: 2
                        }
                    },
                    //sampling: 'max',
                    //areaStyle: {
                    //    normal: {
                    //        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    //            offset: 0,
                    //            color: 'rgb(255, 158, 68)'
                    //        }, {
                    //            offset: 1,
                    //            color: 'rgb(255, 70, 131)'
                    //        }])
                    //    }
                    //},
                    data: compData
                }
            ]
        };
        return option1;
    }

});

