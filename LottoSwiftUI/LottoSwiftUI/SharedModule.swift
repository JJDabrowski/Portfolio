//
//  SharedModule.swift
//  LottoSwiftUI
//
//  Created by Jakub Dąbrowski on 05/03/2022.
//

import Foundation

class SharedModule {
    
    func iterateAndRemove(_ numbers: Set<Int>, in range: ClosedRange<Int>) -> (Set<Int>, Set<Int>){
        
        var numbers = numbers
        
        var results = Set<Int>()
        for _ in range {
            let randomNumbers = numbers.randomElement()!
            results.insert(randomNumbers)
            numbers.remove(randomNumbers)
        }
    return (numbers, results)
    }
}
