import QtQuick 1.0

Rectangle{
    id: myRoot
    width:500;height:500
    anchors.fill:parent
    
    color: "lightblue"
    
    Rectangle {
        id: rect
        anchors { fill: parent; topMargin: 10; leftMargin: 10; rightMargin: 10; bottomMargin: 10 }
        radius:10
        color: "#ddffdd"
        
        Text {
            text: textToShow
            wrapMode: Text.Wrap
            anchors.centerIn: parent
            font.pixelSize: 20
            anchors { fill:parent; topMargin: 5; leftMargin: 5; rightMargin: 5; bottomMargin: 5 }
            clip: true
        }
    }
}
