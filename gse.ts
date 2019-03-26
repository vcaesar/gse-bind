
declare module "gse" {
    export function getVerson(): string;
    export function loadDict(dict: string): void;
    export function addToken(text: string, freq: number, pos?: string): void;
    export function addTokenForce(text: string, freq: number, pos?: string): void;
    export function find(text: string): { freq: number, ok: boolean };
    export function cut(sentence: string, hmm?: boolean): any;
    export function cutAll(sentence: string): any;
    export function cutSearch(sentence: string, hmm?: boolean): string[];
}