import QtQuick 1.0
import com.nokia.meego 1.0

PageStackWindow {
    id: appWindow

    initialPage: mainPage
    MainPage{id: mainPage}


    Menu {
        id: myMenu
        MenuLayout {

            MenuItem {
                text: "Help"
                onClicked: { help.open(); }
            }
            MenuItem {
                text: "About"
                onClicked: { about.open(); }
            }
        }
    }

    QueryDialog {
        id: about
        titleText: "About Acceleration graph"
        message: "This is simple graph from past acceleration of the phone\n" + 
                 "Author: Pauli Sundberg, firstname.lastname@gmail.com"
    }


    QueryDialog {
        id: help
        titleText: "AccelerationGraph Help"
        message: "Showed bars are difference to last acceleration sampled. One measurement has low and high acceleration" + 
                 "value and mean value drawn with green."
    }

}
