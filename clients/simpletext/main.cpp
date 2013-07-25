/*
 * Copyright (c) 2013 Felix Rohrbach <fxrh@gmx.de>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 */


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
