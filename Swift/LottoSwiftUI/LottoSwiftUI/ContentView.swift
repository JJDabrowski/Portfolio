//
//  ContentView.swift
//  LottoSwiftUI
//
//  Created by Jakub Dąbrowski on 05/01/2022.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationView{
            VStack(spacing: 30){
                Text("Symulator Lotto \n Chybił-Trafił")
                    .font(.headline)
                    .foregroundColor(.yellow)
                    .multilineTextAlignment(.center)
                    .padding()
                    .frame(width: 200, height: 150)
                    .background(Rectangle().fill(Color.blue).shadow(radius: 3))
                    .padding(.bottom, 30)
                
                NavigationLink(destination: BigLottoView()){
                    Text("Duży Lotek")
                }
                
                NavigationLink(destination: SmallLottoView()){
                    Text("Mały Lotek")
                }
                
                NavigationLink(destination: EuroJackpotView()){
                    Text("Euro Jackpot")
                }
            }.offset(y: -60)
        }
    }
}

                    

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
