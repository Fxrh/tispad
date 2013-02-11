#include <QtGui/QApplication>
#include <QtDeclarative/QDeclarativeView>
#include <QtDeclarative/QDeclarativeContext>


int main( int argc, char** argv )
{
    QApplication app(argc, argv);
    QStringList args = app.arguments();
    
    if( args.size() != 2 )
    {
        return 1;
    }
    
    QString text(args[1]);
    
    QDeclarativeView view;
    view.setResizeMode(QDeclarativeView::SizeRootObjectToView);
    QDeclarativeContext* context = view.rootContext();
    context->setContextProperty("textToShow", text);
    
    view.setSource(QUrl("qrc:///simpletext.qml"));
    view.show();
    
    return app.exec();
}
