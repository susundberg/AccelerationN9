import QtQuick 1.0
import com.nokia.meego 1.0
import myAccelerationGraph 1.0

Page {
   id: mainPage
   tools: toolbar
   anchors.margins: 10
   orientationLock: PageOrientation.LockLandscape
   
   Column {
      id: col
      spacing: 10
      width: parent.width   
         
      
      AccelerationGraph {
        id: myAccGraph
        objectName: "myAccGraph"
        width: 700
        height: 350
        anchors.centerIn: parent
        }

   }




//*******************************************************



   ToolBarLayout {
      id: toolbar
      
      ToolButtonRow { } //needed, so the menu is on the right side	      
         
      ToolIcon {
         iconId: "toolbar-view-menu" ;
         onClicked: myMenu.open();
      }
   }    

}
